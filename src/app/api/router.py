import aiofiles
import io
import logging
import os
import uuid

from fastapi import APIRouter, UploadFile
from starlette.background import BackgroundTask
from fastapi.responses import StreamingResponse, FileResponse

from app import APP_ROOT_PATH
from app.api.schemas import WordReplacementConfig, WordReplacementRequest, WordReplacementResponse
from app.api.handler import process_input_string
from app.constants import REPLACEMENT_MAP

logger = logging.getLogger("debug-logger")
rt = APIRouter(prefix="/word-replacement", tags=["Word replacement"])


@rt.get("/", response_model=WordReplacementConfig)
async def get_config() -> dict[str, dict[str, str]]:
    """
    Provide word replacement application config
    """
    return dict(config=REPLACEMENT_MAP)


@rt.post("/", response_model=WordReplacementResponse)
async def replace_words_from_payload(payload: WordReplacementRequest) -> dict[str, str]:
    """
    Replace words in input string using word replacement application config
    """
    return dict(processed_str=process_input_string(payload.input_str))


@rt.post("/upload-file")
async def replace_words_from_file_to_file(file: UploadFile) -> FileResponse:
    """
    Replace words from input file using word replacement application config and return new file
    """
    processed_file_content = process_input_string(file.file.read().decode())

    file_ext = file.filename.rsplit(".", maxsplit=1)[-1]
    save_path = os.path.join(APP_ROOT_PATH, 'data', f"{uuid.uuid4()}.{file_ext}")

    async with aiofiles.open(save_path, "w") as f:
        await f.write(processed_file_content)

    return FileResponse(
        path=save_path,
        filename=f"replaced_{file.filename}",
        background=BackgroundTask(lambda: os.remove(save_path))
    )


@rt.post("/upload-stream")
async def replace_words_from_file_to_stream(file: UploadFile) -> StreamingResponse:
    """
    Replace words from input file using word replacement application config and return updated content stream
    """
    processed_file_content = process_input_string(file.file.read().decode())
    return StreamingResponse(content=io.BytesIO(processed_file_content.encode()), media_type="text/plain")
