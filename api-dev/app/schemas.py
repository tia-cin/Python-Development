from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class PostBase(BaseModel):
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True

class PostCreate(PostBase):
    pass