from pydantic import BaseModel, EmailStr
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

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    # created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str