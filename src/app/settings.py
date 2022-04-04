import enum

from pydantic import BaseSettings


class Env(str, enum.Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class Settings(BaseSettings):
    debug: bool = False
    port: int = 8000
    host: str = "0.0.0.0"
    env: Env = Env.DEV

    workers_count: int = 1
    reload: bool = True

    jwk4jwt: str

    class Config:
        env_prefix = "WR_"


settings = Settings()
