from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from uuid import uuid4, UUID
from . import models
from .db import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# classes
class Post(BaseModel):
    id: Optional[UUID]
    title: str
    content: str
    likes: Optional[int] = 0
    private: bool = True


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

# GET routes
@app.get("/")
def root():
    return {
        "message": "Go to '/docs' to read the documentation of the API and get started!"
    }

@app.get("/sqlalchemy")
def testing(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"all_posts": posts}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return {"all_posts": posts}


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
def get_post(id: UUID, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    return {"post_detail": post}

# POST routes
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post, db: Session = Depends(get_db)):
    created_post = models.Posts(**new_post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return {"new_post": created_post}

# DELETE routes
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: UUID, db: Session = Depends(get_db)):
    deleted_post = db.query(models.Posts).filter(models.Posts.id == id)

    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    deleted_post.delete(synchronize_session=False)
    db.commit()
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
