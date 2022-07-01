from fastapi import FastAPI
from . import database, models

from .routers import user
from .routers import post
from .routers import auth
from .routers import vote
from . import config


models.Base.metadata.create_all(bind = database.engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}  


