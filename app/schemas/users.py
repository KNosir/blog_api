from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    user_name: str
    user_privilege_id: int


class User(BaseModel):
    id: int
    user_name: str
    is_active: bool
    user_privilege_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class UserPut(BaseModel):
    user_name: Optional[str] = None
    is_active: Optional[bool] = None
    user_privilege_id: Optional[int] = None


class UserPrivilege(BaseModel):
    id: int
    privilege_title: str
    description: str
    created_at: datetime

    model_config = {"from_attributes": True}
