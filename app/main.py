from fastapi import FastAPI
from app.controllers.posts import router as post_router
from app.controllers.users import router as user_router
from app.controllers.auth import router as auth_router
app = FastAPI()

app.include_router(router=user_router, prefix="/api", tags=["users"])
app.include_router(router=post_router, prefix="/api", tags=["posts"])
app.include_router(router=auth_router, prefix="/api", tags=["auth"])
