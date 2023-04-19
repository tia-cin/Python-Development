from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange

app = FastAPI()

# classes
class Post(BaseModel):
    id: int = 0
    title: str
    content: str
    likes: int = 0
    private: Optional[bool] = True
    rating: Optional[int] = None


user_posts = [{
    "title": "TEST 1",
    "content": "test 1",
    "likes": 0,
    "id": 1
  }, {
    "title": "TEST 2",
    "content": "test 2",
    "likes": 0,
    "id": 2
  }]

def find_post(id):
    for post in user_posts:
        if post['id'] == id:
            return post

# GET routes
@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/posts")
def get_posts():
    return {"posts": user_posts}


# POST routes
@app.post('/posts')
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict['post_id'] = randrange(0, 1000000)
    user_posts.append(post_dict)
    return {"new_post": post_dict}

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": f"Post detail of post {id}"}