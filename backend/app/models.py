from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
# from sqlalchemy.orm import relationship
 
from database import Base

class UserAccount(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    user_name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    password_salt = Column(String)
    password_hash_algorithm = Column(String)
    role_id = Column(Integer, ForeignKey("user_role.role_id"))

class UserRole(Base):
    __tablename__ = "user_role"
    role_id = Column(Integer, primary_key=True)
    role = Column(String)

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None






