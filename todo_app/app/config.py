#!/usr/bin/python3
"""
Handles environment variables
"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASEURL: str
    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRATION: int
    class Config:
        env_file = "./.env"

settings = Settings()
