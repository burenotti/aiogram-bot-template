import os

import dotenv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Config:

    bot_token: str

    debug: bool = True

    webhook_host: str | None = None
    webhook_port: int | None = None
    webhook_path: str = '/bot'

    disable_mongo: bool = False
    mongo_host: str = 'localhost'
    mongo_port: int = 27017


def load_config(path: Path | str) -> Config:
    path = Path(path)
    data = dotenv.dotenv_values(path)
    cfg = {}
    for key in data.keys():
        if value := os.environ.get(key):
            data[key.lower()] = value

    return Config(**data)


config = load_config('.env')
