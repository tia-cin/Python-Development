from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import uuid4, UUID
from sqlalchemy import func
from ..db import get_db

router = APIRouter(prefix='/posts', tags=["Posts"])

# GET routes


@router.get("/")
def get_posts(db: Session = Depends(get_db), curr_user: UUID = Depends(oauth2.get_curr_user), limit: int = 5, skip: int = 0, search: Optional[str] = ""):
    posts = db.query(models.Posts, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Posts.id, isouter=True).group_by(models.Posts.id).filter(
        models.Posts.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.get("/lastest", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user), limit: int = 5):
    posts = db.query(models.Posts).order_by(
        models.Posts.created_at).limit(limit).all()
    return posts


@router.get("/public", response_model=List[schemas.Post])
def get_lastest_posts(db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    posts = db.query(models.Posts).filter(models.Posts.private == False).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Public Posts not found"
        )

    return posts


@router.get('/{id}', response_model=schemas.PostOut)
def get_post(id: UUID, db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    post = db.query(models.Posts, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Posts.id, isouter=True).group_by(models.Posts.id).filter(models.Posts.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    if post.owner_id != oauth2.get_curr_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not Authorized to perform requested action"
        )

    return post

# POST routes


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(new_post: schemas.PostCreate, db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    created_post = models.Posts(owner_id=curr_user.id, **new_post.dict())
    db.add(created_post)
    db.commit()
    db.refresh(created_post)
    return created_post

# DELETE routes


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: UUID, db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    deleted_post = db.query(models.Posts).filter(models.Posts.id == id)

    if deleted_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} was not found"
        )

    if deleted_post.owner_id != oauth2.get_curr_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not Authorized to perform requested action"
        )

    deleted_post.delete(synchronize_session=False)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    db.commit()

# PUT routes


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: UUID, post: schemas.PostCreate, db: Session = Depends(get_db), curr_user: str = Depends(oauth2.get_curr_user)):
    updated_post = db.query(models.Posts).filter(models.Posts.id == id).first()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post {id} was not found")

    if updated_post.owner_id != oauth2.get_curr_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not Authorized to perform requested action"
        )

    updated_post.update(post.dict(), synchronize_session=False)
    db.commit()
    return updated_post
