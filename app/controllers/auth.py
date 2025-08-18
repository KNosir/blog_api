from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from app.database import get_db
from app.schemas.users import UserCreate, User
from app.models.users import User as UserORM
from app.security import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES
from app.services.users import service_get_user_by_user_name, service_post_user
# from app.models.users import User


router = APIRouter()


@router.post("/auth/signup", response_model=User)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await service_get_user_by_user_name(user.user_name, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return await service_post_user(UserORM(**user.model_dump()), db)


@router.post("/auth/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/logout")
async def logout():
    pass
