from contextlib import AbstractAsyncContextManager, asynccontextmanager
import logging
from typing import Callable, Final
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from typing_extensions import AsyncGenerator


Base = declarative_base()

logger = logging.getLogger(__name__)




class PostgresDatabase:
    
    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(db_url)
        self._async_session_maker = async_sessionmaker(bind=self._engine, expire_on_commit=False)
        
    async def create_db_tables(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            

    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._async_session_maker() as session:
            try: 
                yield session
            except Exception as e:
                logging.exception("Session rollback due to exception}")
                await session.rollback()
                raise
            finally:
                await session.close()

