from logging.config import dictConfig
from pathlib import Path

from app.logging_config import dict_config

APP_ROOT_PATH = Path(__file__).parent
APP_NAME: str = "Word replacement API case"
APP_DESCRIPTION: str = (
    "Assignment to build an API that will use a string as input"
    " and does a find and replace for certain words and outputs the result"
)

dictConfig(dict_config)
