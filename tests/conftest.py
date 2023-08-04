import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient

from sqlalchemy import text, create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.main import app
from src.models.contact import Base
from src.api.dependencies.db import get_dbsession
from src.config import settings


sync_test_engine = create_engine(settings.uri_test_db_connection, poolclass=NullPool)
sync_test_session = sessionmaker(sync_test_engine, expire_on_commit=False)

engine_test = create_async_engine(settings.uri_test_db_connection, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session')
async def init_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(autouse=True, scope='session')
async def add_data(init_database):
    app.dependency_overrides[get_dbsession] = override_get_async_session
    async with engine_test.connect() as conn:
        copy_query = text(
            f"""
            COPY 
                contacts (first_name, last_name, email) 
            FROM '{settings.CONTACT_PATH}' 
                DELIMITER ',' 
                CSV HEADER
            """
        )
        update_tsv_query = text(
            """UPDATE contacts SET tsv = to_tsvector('english', concat(email, ' ', first_name, ' ', last_name))"""
        )
        await conn.execute(copy_query)
        await conn.execute(update_tsv_query)
        await conn.commit()


@pytest_asyncio.fixture(scope="session")
async def aclient() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api/v1") as ac:
        yield ac
