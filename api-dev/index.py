from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange

app = FastAPI()

# classes
class Comment(BaseModel):
    user: str = "user comment"
    comment: str
    likes: int = 0
    comment_id: int = 0

class Post(BaseModel):
    post_id: int = 0
    title: str
    content: str
    likes: int = 0
    user: str = 'user'
    comments: Comment
    private: Optional[bool] = True
    rating: Optional[int] = None

class User(BaseModel):
    user_id: int = 0
    username: str
    email: str
    followers: Optional[int] = 0
    following: Optional[int] = 0
    posts: List[Post] = None

user_posts = [{
    "title": "TEST 1",
    "content": "test 1",
    "likes": 0,
    "user": "user test 1",
    "comments": {
      "user": "user comment 1",
      "comment": "testing 1",
      "likes": 0
    }
  }, {
    "title": "TEST 2",
    "content": "test 2",
    "likes": 0,
    "user": "user test 2",
    "comments": {
      "user": "user comment 2",
      "comment": "testing 2",
      "likes": 0
    }
  }]

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
