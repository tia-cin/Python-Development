from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Comment(BaseModel):
    user: str
    comment: str
    likes: int

class Post(BaseModel):
    title: str
    content: str
    likes: int
    user: str
    comments: Comment



@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/")
def get_posts():
    return {"posts": [1,2,3,4]}

@app.post('/posts')
def create_post(new_post: Post):
    print(payload)
    return {"newPost": f"title {payload['title']} content: {payload['content']}"}

