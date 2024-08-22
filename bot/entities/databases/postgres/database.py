from typing import AsyncGenerator

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:


    def __init__(
        self, host: str, port: int, password: str, user: str, database: str
    ) -> None: 
        self.engine = create_async_engine(
            url = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}',
            echo = True
        )

        self.async_session = sessionmaker(
            bind = self.engine, class_ = AsyncSession, expire_on_commit=False
        )


    @asynccontextmanager
    async def get_session(self)->AsyncGenerator[AsyncSession, None]:
        session: AsyncSession = self.async_session()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


    async def init_models(self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)