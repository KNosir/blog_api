from pydantic import BaseModel
from datetime import datetime
from typing import Optional



class PostCreate(BaseModel):
    title: str
    description: str


class Post(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {"from_attributes": True}


class PostPut(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
