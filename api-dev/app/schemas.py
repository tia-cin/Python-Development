from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True