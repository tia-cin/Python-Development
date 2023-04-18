from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# classes
class Comment(BaseModel):
    user: str = "user comment"
    comment: str
    likes: int = 0

class Post(BaseModel):
    title: str
    content: str
    likes: int = 0
    user: str = 'user'
    comments: Comment
    private: Optional[bool] = True
    rating: Optional[int] = None

# GET routes
@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/")
def get_posts():
    return {"posts": [1,2,3,4]}


# POST routes
@app.post('/posts')
def create_post(new_post: Post):
    print(new_post)
    return {"new post"}
    # return {"newPost": f"title {new_post['title']} content: {new_post['content']}"}

