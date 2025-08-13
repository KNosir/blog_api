from fastapi import FastAPI
from app.controllers.posts import router as post_router
app = FastAPI()

app.include_router(router=post_router, prefix="/api", tags=["posts"])
