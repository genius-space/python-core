import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.db import engine, get_async_session
from app.app import app
from app.user_models import Base
from app.config import settings
from httpx import AsyncClient
import asyncio
from typing import AsyncGenerator
from sqlalchemy.pool import NullPool

from sqlalchemy import select
from app.user_models import User


DATABASE_URL = settings.DATABASE_URL
engine_test = create_async_engine(DATABASE_URL, poolclass=NullPool, echo=False)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="session")
def token_storage():
    return {}


@pytest.fixture(scope="session")
def user_id_storage():
    return {}


@pytest.fixture(scope="session")
async def get_token(token_storage):
    token = token_storage.get("token")
    assert token is not None
    yield token


@pytest.fixture(scope="session")
async def get_user_id(user_id_storage):
    user_id = user_id_storage.get("id")
    assert user_id is not None
    yield user_id


@pytest.fixture
async def get_user_by_field():
    async def _get_user_by_field(field, value):
        async with async_session_maker() as session:
            filter_condition = getattr(User, field) == value
            result = await session.execute(select(User).filter(filter_condition))
            return result.scalar_one_or_none()
    return _get_user_by_field