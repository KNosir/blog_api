from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.schemas.posts import PostCreate, PostGet, PostPut
from app.services.posts import service_get_posts, service_get_posts_by_id, service_post_posts, service_delete_posts, service_put_posts
from app.models.posts import Post
from app.models.users import User
from app.services.auth import get_current_user
from app.utils import logger


router = APIRouter()


@router.get("/")
async def main():
    return JSONResponse({"message": "ok"})


@router.get("/posts", response_model=list[PostGet])
async def route_get_posts(db: AsyncSession = Depends(get_db)):
    return await service_get_posts(db)


@router.get("/posts/{id}", response_model=list[PostGet])
async def route_get_posts_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await service_get_posts_by_id(id, db)


@router.post("/posts", response_model=PostGet)
async def route_post_posts(post: PostCreate,
                           db: AsyncSession = Depends(get_db),
                           current: User = Depends(get_current_user)):  # ------
    logger.debug(f"Current user: {current.id}, {current.user_name}")
    return await service_post_posts(Post(**post.model_dump()), db)


@router.put("/posts/{id}", response_model=PostGet)
async def route_put_posts(id: int, post: PostPut, db: AsyncSession = Depends(get_db)):
    return await service_put_posts(id, post, db)


@router.delete("/post/{id}")
async def route_delete_posts(id: int, db: AsyncSession = Depends(get_db)):
    return await service_delete_posts(id, db)
