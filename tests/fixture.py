"""Pytest plugins"""

import pytest
import pytest_asyncio
from unittest.mock import MagicMock
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from tronpy import Tron
from ..models import Base


DATABASE_URL = "sqlite+aiosqlite:///./test.db"


@pytest_asyncio.fixture(scope="session")
async def engine():
    """Fixture create test engine"""

    engine = create_async_engine(DATABASE_URL, echo=False)
    yield engine


@pytest_asyncio.fixture(scope="function")
async def session(engine):
    """Fixture create test session"""

    async_session = async_sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as s:
        yield s

    await s.rollback()
    await s.close()


@pytest.fixture
def mock_tron(mocker):
    """Fixture for mocked method 'get_account' from tron client"""

    mock_get_account = MagicMock()
    mocker.patch.object(Tron, 'get_account', new=mock_get_account)
    return mock_get_account
