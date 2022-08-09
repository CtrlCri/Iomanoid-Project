# Python
from datetime import datetime
from email.policy import default

#Pydantic
from pydantic import BaseModel, EmailStr, Field

class Subscriber(BaseModel):
    email: EmailStr = Field(...)
    created_at: datetime = Field(default=datetime.now())

