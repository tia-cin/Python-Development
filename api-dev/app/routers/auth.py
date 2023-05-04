from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import db, schemas, models

router = APIRouter(tags=["Authentication"])

@router.post("/auth")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(db.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Invalid Credential"
        )
    