from pydantic import BaseModel, Field


class WordReplacementConfig(BaseModel):
    config: dict[str, str]


class WordReplacementRequest(BaseModel):
    input_str: str

    class Config:
        schema_extra = {
            "example": {
                "input_str": "We really like the new security features of Google Cloud",
            }
        }


class WordReplacementResponse(BaseModel):
    processed_str: str

    class Config:
        schema_extra = {
            "example": {
                "input_str": "We really like the new security features of Google© Cloud",
            }
        }
