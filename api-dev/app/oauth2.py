from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from . import schemas, db, models
from jose import JWSError, jwt
from .config import setting

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth')

SECRET_KEY = setting.secret_key
ALGORITHM = setting.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = setting.access_token_expire_minutes


def create_access_token(data: dict):
    encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({"exp": expire})

    encoded = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)
    except JWSError as error:
        print(error)
        raise credentials_exception
    except AssertionError as error:
        print(error)

    return token_data


def get_curr_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could NOT Validate Credentials",
        headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
