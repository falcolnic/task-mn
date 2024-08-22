from os import environ as env

from pydantic_settings import BaseSettings
from pydantic import Field


class BotConfig(BaseSettings):
    token: str = Field(env.get('TOKEN'))

    redis_host: str = Field(env.get('REDIS_HOST'))
    redis_port: int = Field(env.get('REDIS_PORT'))

    db_host: str = Field(env.get('POSTGRES_HOST'))
    db_port: int = Field(env.get('POSTGRES_PORT'))
    db_user: str = Field(env.get('POSTGRES_USER'))
    db_password: str = Field(env.get('POSTGRES_PASSWORD'))
    db_database: str = Field(env.get('POSTGRES_DB'))