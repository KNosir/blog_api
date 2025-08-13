from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timezone


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))
