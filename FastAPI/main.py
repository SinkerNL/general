from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    """
    Defines the types and values for the create posts function
    """
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {'title': 'title of post 1', 'content': 'content of post 1', 'id': 1},
    {'title': 'favorite foods', 'content': 'I like pizza', 'id': 2}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {'data': my_posts}

"""
Payload is the param, body will make it into dict
"""
@app.post("/posts")
def create_posts(post: Post):
    print(post.title)
    print(post.dict())
    return {"data": str(post.dict())}