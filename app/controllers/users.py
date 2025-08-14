from fastapi import APIRouter, Depends
from app.schemas.users import UserGet, UserPrivilege
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.users import service_get_users, service_get_user_privileges, service_get_user_by_id

router = APIRouter()


@router.get("/users", response_model=list[UserGet])
async def get_users(db: AsyncSession = Depends(get_db)):
    return await service_get_users(db)


@router.get("/users/{id}", response_model=list[UserGet])
async def get_user_by_id(id: int, db: AsyncSession = Depends(get_db)):
    return await service_get_user_by_id(id, db)

# @router.put("/users/{id}", response_model=UserGet)
# async def update_user(id: int, user: UserPut, db: AsyncSession = Depends(get_db)):
#     return await service_update_user(id, user, db)

# @router.delete("/users/{id}", response_model=UserGet)
# async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
#     return await service_delete_user(id, db)


@router.get("/user_privileges", response_model=list[UserPrivilege])
async def get_user_privileges(db: AsyncSession = Depends(get_db)):
    return await service_get_user_privileges(db)

# @router.get("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)

# @router.put("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)

# @router.delete("/user_privileges/{id}", response_model=list[UserPrivilege])
# async def get_user_privileges(db: AsyncSession = Depends(get_db)):
#     return await service_get_user_privileges(db)
