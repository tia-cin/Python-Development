from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# to be changed for security
SQLALCHEMY_DB_URL = 'postgresql://postgres:data123@localhost/apidev'

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    d = SessionLocal()
    try:
        yield db
    finally:
        db.close()