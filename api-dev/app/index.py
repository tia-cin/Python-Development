from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from uuid import uuid4, UUID
from . import models, schemas, utils
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



@app.get('/users/{id}', response_model=schemas.UserOut)
def get_user(id: UUID, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {id} was not found"
        )

    return user



@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(new_user: schemas.UserBase, db: Session = Depends(get_db)):
    hashed_psw = utils.hash(new_user.password)
    new_user.password = hashed_psw

    created_user = models.User(**new_user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user

