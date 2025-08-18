from app.models.users import User, UserPrivilege
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


async def service_get_users(db: AsyncSession):
    result = await db.execute(select(User).where(and_(User.is_active == True, User.deleted_at == None)))  # noqa: E712
    return result.scalars().all()


async def service_get_user_by_id(id: int, db: AsyncSession):
    result = await db.execute(select(User).where(and_(User.is_active.is_(True), User.deleted_at.is_(None), User.id == id)))  # noqa: E712
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")

    return result.scalars().all()


async def service_get_user_privileges(db: AsyncSession):
    result = await db.execute(select(UserPrivilege).where(User.deleted_at == None))
    return result.scalars().all()