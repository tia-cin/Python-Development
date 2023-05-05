from .. import models, schemas, utils
from ..db import get_db
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from uuid import uuid4, UUID

router = APIRouter(prefix='/users', tags=["Users"])

# GET routes


@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id: UUID, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {id} was not found"
        )

    return user


# POST routes
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(new_user: schemas.UserBase, db: Session = Depends(get_db)):
    hashed_psw = utils.hash(new_user.password)
    new_user.password = hashed_psw

    created_user = models.User(**new_user.dict())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user
