from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import schemas, database, utils, models
from sqlalchemy.orm import Session

from .routers import user
from .routers import post

models.Base.metadata.create_all(bind = database.engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host = "localhost", database = 'fastapi', user='fastapiuser', password='sinterklaas', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print(f'error: {error}')
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}  


