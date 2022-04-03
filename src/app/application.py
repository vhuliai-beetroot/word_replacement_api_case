import logging

from fastapi import FastAPI, Depends
from fastapi.responses import UJSONResponse
from starlette import status

from app import APP_NAME, APP_DESCRIPTION
from app.api.router import rt
from app.auth import authorized_request
from app.schemas import AppInfo
from app.utils import read_version

logger = logging.getLogger("debug-logger")

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=read_version(),
    default_response_class=UJSONResponse,
)

responses = {
    status.HTTP_401_UNAUTHORIZED: {'description': 'Unauthorized'},
}

app.include_router(rt, responses=responses, dependencies=[Depends(authorized_request)])


@app.get("/", response_model=AppInfo)
async def root() -> dict:
    """
    Provides application information and version
    """
    return {'name': app.title, 'description': app.description, 'api_version': app.version}


@app.get("/health")
def health_check() -> None:
    """
    Checks the health of the application.
    """
