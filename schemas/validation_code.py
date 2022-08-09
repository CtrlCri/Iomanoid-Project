# Python
from datetime import datetime
from email.policy import default



#Pydantic
from pydantic import BaseModel, Field

class ValidationCode(BaseModel):
    code: UUID = Field(...)
    enabled: bool = Field(default=False)
