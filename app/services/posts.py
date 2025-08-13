from sqlalchemy.ext.asyncio import AsyncSession
from app.models.posts import Post
from sqlalchemy import and_, select
from fastapi import HTTPException
from datetime import datetime, timezone


async def service_get_posts(db: AsyncSession):
    result = await db.execute(select(Post).where(Post.deleted_at == None))
    return result.scalars().all()


async def service_get_posts_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(Post).where(Post.deleted_at == None, Post.id == id))
    return result.scalars().all()


async def service_post_posts(post: Post, db: AsyncSession):
    post.user_id = 1
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def service_put_posts(id: int, post: Post, db: AsyncSession):
    conditions = and_(Post.id == id, Post.deleted_at == None)
    result = await db.execute(select(Post).where(conditions))
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(status_code=404, detail="Post not found")

    for field, value in post.model_dump(exclude_unset=True).items():
        setattr(result, field, value)
    result.updated_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(result)
    return result


async def service_delete_posts(id: int, db: AsyncSession):
    result = await db.execute(select(Post).where(Post.id == id))
    result = result.scalar_one_or_none()

    if not result:
        raise HTTPException(status_code=404, detail="Post not found")

    result.deleted_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(result)
    return {"message": "done"}
