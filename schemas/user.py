#Python
from uuid import UUID
from typing import Optional
from datetime import datetime

# Pydantic
from pydantic import BaseModel, Field, EmailStr


# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=20
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None) 

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

class User(UserBase):
    pass 
    