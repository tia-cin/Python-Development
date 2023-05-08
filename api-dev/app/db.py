from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .config import setting

SQLALCHEMY_DB_URL = f'postgresql://{setting.db_un}:{setting.db_psw}@{setting.db_host}:{setting.db_port}/{setting.db_name}'
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
