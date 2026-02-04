from fastapi import FastAPI
from .database import Base, engine
from .routers import users, posts, comments, auth
from . import models



app=FastAPI()

# создаём таблицы в базе
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(auth.router)



@app.get("/test")
def test():
    return{"message":"Hello"}


