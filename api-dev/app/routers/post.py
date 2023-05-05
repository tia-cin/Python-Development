from .. import models, schemas, oauth2
from ..db import get_db
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4, UUID

router = APIRouter(prefix='/posts', tags=["Posts"])

# GET routes
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    posts = db.query(models.Posts).all()
    return posts


@router.get("/lastest", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    posts = db.query(models.Posts).order_by(models.Posts.created_at).limit(5).all()
    return posts

@router.get("/public", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    posts = db.query(models.Posts).filter(models.Posts.private == False).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Public Posts not found"
        )
    
    return posts


@router.get('/{id}', response_model=schemas.Post)
def get_post(id: UUID, db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    return post

# POST routes
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(new_post: schemas.PostCreate, db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    created_post = models.Posts(**new_post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post

# DELETE routes
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: UUID, db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    deleted_post = db.query(models.Posts).filter(models.Posts.id == id)

    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    deleted_post.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    db.commit()

# PUT routes
@router.put("/{id}", response_model=schemas.Post)
def update_post(id: UUID, post: schemas.PostCreate, db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_curr_user)):
    updated_post = db.query(models.Posts).filter(models.Posts.id == id)

    if updated_post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {id} was not found")

    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post.first()
