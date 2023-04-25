from .db import Base
from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Posts(Base):
    __tablename__ = "posts"

    id = Column(UUID, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    likes = Column(Integer, server_default='0')
    private = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
