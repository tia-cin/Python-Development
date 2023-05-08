from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from uuid import UUID


class PostBase(BaseModel):
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    # created_at: datetime

    class Config:
        orm_mode = True


class Post(PostBase):
    created_at: datetime
    id: UUID
    owner_id: UUID
    owner: UserOut

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
