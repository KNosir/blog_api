from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import User as UserGet, UserPrivilege
from app.database import get_db
from app.services.users import service_get_users, service_get_user_privileges, service_get_user_by_id
from app.models.users import User
from app.services.auth import get_current_user
from app.security import check_admin_by_id

router = APIRouter()


@router.get("/users", response_model=list[UserGet])
async def get_users(db: AsyncSession = Depends(get_db),
                    current: User = Depends(get_current_user)):
    if await check_admin_by_id(current.id, db):
        return await service_get_users(db)
    raise HTTPException(status_code=403, detail="Not enough permissions")


@router.get("/users/{id}", response_model=list[UserGet])
async def get_user_by_id(id: int, db: AsyncSession = Depends(get_db), current: User = Depends(get_current_user)):
    if await check_admin_by_id(current.id, db):
        return await service_get_user_by_id(id, db)
    raise HTTPException(status_code=403, detail="Not enough permissions")

# @router.put("/users/{id}", response_model=UserGet)
# async def update_user(id: int, user: UserPut, db: AsyncSession = Depends(get_db)):
#     return await service_update_user(id, user, db)

# @router.delete("/users/{id}", response_model=UserGet)
# async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
#     return await service_delete_user(id, db)


@router.get("/user_privileges", response_model=list[UserPrivilege])
async def get_user_privileges(db: AsyncSession = Depends(get_db), current: User = Depends(get_current_user)):
    if await check_admin_by_id(current.id, db):
        return await service_get_user_privileges(db)
    raise HTTPException(status_code=403, detail="Not enough permissions")

# @router.get("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)

# @router.put("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)

# @router.delete("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)
