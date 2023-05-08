from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# from psycopg2.extras import RealDictCursor
# import psycopg2
# import time

# to be changed for security
SQLALCHEMY_DB_URL = 'postgresql://postgres:data123@localhost/apidev'

engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# DataBase connection
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="apidev",
#             user="postgres",
#             password="data123",
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("Database connected")
#         break
#     except Exception as error:
#         print("Connection failed, Error:", error)
#         time.sleep(2)
