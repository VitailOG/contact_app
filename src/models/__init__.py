from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings


SQLALCHEMY_ENGINE_OPTIONS = {"echo": False, "future": True}

# Create engines
async_engine = create_async_engine(
    settings.uri_db_connection, **SQLALCHEMY_ENGINE_OPTIONS
)

engine = create_engine(settings.uri_db_connection, **SQLALCHEMY_ENGINE_OPTIONS)

# Create sessions
session = sessionmaker(engine, expire_on_commit=False)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)
