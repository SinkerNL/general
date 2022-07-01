from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import database, models

from .routers import user
from .routers import post
from .routers import auth
from .routers import vote
from . import config


models.Base.metadata.create_all(bind = database.engine)

# origins = ["https://www.google.com"] # only google can ask
origins = ["*"] # all sites can access

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}  


