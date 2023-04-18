from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello API"}

@app.get("/")
def get_posts():
    return {"posts": [1,2,3,4]}

@app.post('/posts')
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"newPost": f"title {payload['title']} content: {payload['content']}"}