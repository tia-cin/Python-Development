from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Comment(BaseModel):
    user = "user comment"
    comment: str
    likes = 0

class Post(BaseModel):
    title: str
    content: str
    likes = 0
    user = 'user'
    comments: Comment



@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/")
def get_posts():
    return {"posts": [1,2,3,4]}

@app.post('/posts')
def create_post(new_post: Post):
    print(new_post)
    return {"new post"}
    # return {"newPost": f"title {new_post['title']} content: {new_post['content']}"}

