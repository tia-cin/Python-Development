from .routers import post, user, auth
from fastapi import FastAPI
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
