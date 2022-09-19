from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()


# defining the post model
class Post(BaseModel):
    title: str
    content: str


posts = [
    {
        "title": "this is post1 title",
        "content": "this is very awesome post",
        "id": 1
    },
    {
        "title": "this is post number 2",
        "content": "this is the content for the post number 2",
        "id" : 2
    },
    {
        "title": "this is the another title for the third post",
        "content": "this is the content for the third post",
        "id": 3
    }
]


@app.get('/posts')
async def get_all_posts():
    return {"data": posts}


@app.get('/posts/{_id}')
def get_post_by_id(_id: int):
    index = None
    for idx, item in enumerate(posts):
        if item.get('id') == _id:
            index = idx
            break
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {_id} not found")
    return {"data": posts[index]}


@app.post('/posts')
def create_post(post: Post):
    post_dict = post.dict()
    posts.append(post_dict)
    return {"message": "created"}





