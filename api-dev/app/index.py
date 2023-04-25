from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import uuid
from . import models
from .db import engine, SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# classes
class Post(BaseModel):
    id: int = 0
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True

# DB Dependency
def get_db():
    d = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DataBase connection
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

# functions for testing
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
    return {
        "message": "Go to '/docs' to read the documentation of the API and get started!"
    }

@app.get("/sqlalchemy")
def testing(db: Session = Depends(get_db)):
    return {"status": "success"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts;""")
    posts = cursor.fetchall()
    return {"posts": posts}


@app.get("/posts/lastest")
def get_lastest_posts():
    cursor.execute("""SELECT * FROM posts ORDER BY created_at LIMIT 5;""")
    posts = cursor.fetchall()
    return {"lastest_posts": posts}

@app.get("/posts/public")
def get_lastest_posts():
    cursor.execute("""SELECT * FROM posts WHERE private = false;""")
    posts = cursor.fetchall()
    return {"public_posts": posts}


@app.get('/posts/{id}')
def get_post(id: str):
    cursor.execute("""SELECT * FROM posts WHERE id = %s;""", (id,))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )
    return {"post_detail": post}

# POST routes
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    cursor.execute(
        """INSERT INTO posts (id, title, content, private) VALUES (%s, %s, %s, %s) RETURNING *;""",
        (str(uuid.uuid4()), new_post.title, new_post.content, new_post.private)
    )
    created_post = cursor.fetchone()
    conn.commit()
    return {"new_post": created_post}

# DELETE routes
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: str):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""", (id,))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# PUT routes
@app.put("/posts/{id}")
def update_post(id: str, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, private = %s WHERE id = %s RETURNING *;""", 
        (post.title, post.content, post.private, id)
    )
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {id} was not found")
    return {"updated_post": updated_post}
