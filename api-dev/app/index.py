from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

# classes
class Post(BaseModel):
    id: int = 0
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True

while True:
    try:
        conn = psycopg2.connect(
            host="localhost", 
            database="apidev", 
            user="postgres", 
            password="data123", 
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connected")
        break
    except Exception as error:
        print("Connection failed, Error:", error)
        time.sleep(2)


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

def find_index_post(id):
    for i, p in enumerate(user_posts):
        if p['id'] == id:
            return i

# GET routes
@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/posts")
def get_posts():
    return {"posts": user_posts}

@app.get("/posts/lastest")
def get_lastest_posts():
    post = user_posts[len(user_posts)-1]
    return {"lastest_posts": post}

@app.get('/posts/{id}')
def get_post(id: int, res: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    return {"post_detail": post}

# POST routes
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 1000000)
    user_posts.append(post_dict)
    return {"new_post": post_dict}

# DELETE routes
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    user_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# PUT routes
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    user_posts[index] = post_dict
    return {"updated_post": post_dict}