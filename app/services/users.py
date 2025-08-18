from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from datetime import datetime, timezone

from app.models.users import User, UserPrivilege
from app.security import hashed_password


async def service_get_users(db: AsyncSession):
    result = await db.execute(select(User).where(and_(User.is_active == True, User.deleted_at == None)))  # noqa: E712
    return result.scalars().all()


async def service_get_user_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(User).where(and_(User.is_active.is_(True), User.deleted_at.is_(None), User.id == id)))  # noqa: E712
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")

    return result.scalars().all()


async def service_get_user_by_user_name(user_name: str, db: AsyncSession):
    result = await db.execute(select(User).where(and_(User.is_active.is_(True), User.deleted_at.is_(None), User.user_name == user_name)))  # noqa: E712
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result.scalars().first()


async def service_get_user_privileges(db: AsyncSession):
    result = await db.execute(select(UserPrivilege).where(User.deleted_at == None))
    return result.scalars().all()


async def service_post_user(user: User, db: AsyncSession):
    hashed_pass = await hashed_password(user.password)
    new_user = User(user_name=user.user_name,
                    password=hashed_pass,
                    user_privilege_id=user.user_privilege_id,
                    is_active=True,
                    created_at=datetime.now(timezone.utc))

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
