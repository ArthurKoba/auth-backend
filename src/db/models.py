from typing import Optional, Tuple, List, Any, TypeVar, Type
from sqlalchemy import Column, Integer, String, DateTime, select
from sqlalchemy.orm import selectinload

from .base import Base
from .utils import utcnow

TBase = TypeVar("TBase", bound="BaseModel")


class BaseModel(Base):
    __abstract__ = True

    @classmethod
    def _get_query(cls, prefetch: Optional[Tuple[str, ...]] = None, options: Optional[List[Any]] = None) -> Any:
        query = select(cls)
        if prefetch:
            if not options:
                options = []
            options.extend(selectinload(getattr(cls, x)) for x in prefetch)
            query = query.options(*options).execution_options(populate_existing=True)
        return query


class Users(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    nickname = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    @classmethod
    async def all(cls: Type[TBase]) -> List["Users"]:

        return []


