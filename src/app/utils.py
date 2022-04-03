import os

from app import APP_ROOT_PATH


def read_version() -> str:
    with open(os.path.join(APP_ROOT_PATH, 'VERSION'), mode='r') as f:
        return f.read()
