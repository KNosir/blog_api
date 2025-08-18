from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.users import User
from app.schemas.users import UserGet
from sqlalchemy.ext.asyncio import AsyncSession
from app.security import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException, status
from datetime import timedelta
from app.database import get_db


router = APIRouter()


@router.post("/auth/signup")
async def signup():
    pass


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
