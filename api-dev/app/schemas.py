from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    created_at: datetime
    id: UUID
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: int = 0
    is_sale: bool
    inventory: int = 0