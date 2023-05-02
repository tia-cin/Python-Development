from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from uuid import uuid4, UUID
from . import models, schemas
from .db import engine, get_db
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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
@app.get("/posts", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).all()
    return posts


@app.get("/posts/lastest", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).order_by(models.Posts.created_at).limit(5).all()
    return posts

@app.get("/posts/public", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Posts).filter(models.Posts.private == False).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Public Posts not found"
        )
    
    return posts


@app.get('/posts/{id}', response_model=schemas.Post)
def get_post(id: UUID, db: Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    return post

# POST routes
@app.post('/posts', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(new_post: schemas.PostCreate, db: Session = Depends(get_db)):
    created_post = models.Posts(**new_post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post

@app.post('/users', status_code=status.HTTP_201_CREATED)
def create_user(new_user: schemas.UserBase, db: Session = Depends(get_db)):
    created_user = models.User(**new_user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user

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
@app.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: UUID, post: schemas.PostCreate, db: Session = Depends(get_db)):
    updated_post = db.query(models.Posts).filter(models.Posts.id == id)

    if updated_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {id} was not found")

    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post.first()
