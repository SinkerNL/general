from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

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

def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {'data': my_posts}

"""
Payload is the param, body will make it into dict
"""
# when creating a post, status code should be 201!!
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    print(post.title)
    print(post.dict())
    my_posts.append(post_dict)
    return {"data": post_dict}

# Id is a path parameter, id is the id of a specific post
@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int, response: Response):
    post = find_posts(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}")
def delete_post(id: int, status_code = status.HTTP_204_NO_CONTENT):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id: {id} was not found")
    my_posts.pop(index)
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"Post with id: {id} was not found")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}