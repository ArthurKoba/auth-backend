from contextvars import ContextVar
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from .base import async_session


session_context_var: ContextVar[Optional[AsyncSession]] = ContextVar("_session", default=None)


async def set_db():
    db = async_session()
    token = session_context_var.set(db)
    try:
        yield
    finally:
        await db.close()
        session_context_var.reset(token)


def get_db():
    session = session_context_var.get()
    if session is None:
        raise Exception("Missing session")
    return session