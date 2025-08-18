from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from typing import Union, Any
from jose import jwt
from datetime import datetime, timedelta, timezone
from app.models.users import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from fastapi import HTTPException

load_dotenv()
salt = getenv("SALT")

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"
JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = getenv('JWT_REFRESH_SECRET_KEY')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def hashed_password(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_access_token(data: dict, expires_delta: int = None) -> str:
    to_encode = data.copy()
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(
            timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expires_delta})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + expires_delta
    else:
        expires_delta = datetime.now(
            timezone.utc) + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> dict[str, Any]:
    return jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[ALGORITHM]
    )


async def get_user(db: AsyncSession, username: str):
    condition = and_(
        User.user_name == username,
        User.deleted_at.is_(None),
        User.is_active.is_(True)
    )

    result = await db.execute(select(User).where(condition))
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result.scalars().first()


async def authenticate_user(db: AsyncSession, username: str, password: str):
    user = await get_user(db, username)
    if not user:
        return False
    if not await verify_password(password, user.password):
        return False

    return user


async def check_admin_by_id(db: AsyncSession, id: int) -> bool:
    condition = and_(
        User.id == id,
        User.user_privilege_id == 1,
        User.deleted_at.is_(None),
        User.is_active.is_(True)
    )

    result = await db.execute(select(User).where(condition))
    return result.scalars().first() is not None
