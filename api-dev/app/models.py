from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from .db import Base
import uuid


class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, server_default=text('gen_random_uuid()'))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    private = Column(Boolean, server_default='TRUE')
    likes = Column(Integer, server_default='0')
    content = Column(String, nullable=False)
    title = Column(String, nullable=False)

    owner_id = Column(UUID(as_uuid=True), ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    ownner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, server_default=text('gen_random_uuid()'))
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
