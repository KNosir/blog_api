from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    is_active = Column(Boolean, default=True)
    user_privilege_id = Column(Integer, ForeignKey(
        "user_privileges.id", ondelete="SET NULL"), nullable=True)
    user_privilege = relationship("UserPrivilege", back_populates="users")
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))


class UserPrivilege(Base):
    __tablename__ = "user_privileges"

    id = Column(Integer, primary_key=True, index=True)
    privilege_title = Column(String)
    description = Column(String)
    users = relationship("User", back_populates="user_privilege")
    created_at = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    deleted_at = Column(DateTime(timezone=True))
