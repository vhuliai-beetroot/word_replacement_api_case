from pydantic import BaseModel


class AppInfo(BaseModel):
    name: str
    description: str
    api_version: str
