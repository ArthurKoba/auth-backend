from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from configs import DB_DSN, DB_ECHO, DB_POOL_SIZE, DB_MAX_OVERFLOW


engine = create_async_engine(
    DB_DSN,
    echo=DB_ECHO,
    pool_size=DB_POOL_SIZE,
    max_overflow=DB_MAX_OVERFLOW,
    future=True,
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession, future=True)
metadata = MetaData()
Base = declarative_base(metadata=metadata)
