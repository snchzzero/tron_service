"""Init connection to database"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, \
    async_sessionmaker, AsyncEngine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False)

async_session_local = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
