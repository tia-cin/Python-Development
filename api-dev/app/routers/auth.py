from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from ..db import get_db

router = APIRouter(tags=["Authentication"])

@router.post("/auth")
def login(db: Session = Depends(get_db)):
    return