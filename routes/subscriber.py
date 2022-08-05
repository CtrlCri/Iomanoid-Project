
# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path

#
from models.index import subscribers
from config.db import conn
from schemas.index import Subcriber

user = APIRouter()


## Subscribers
### 

@subscriber.post(
    path="/subscribe", 
    status_code=status.HTTP_200_OK,
    tags=["Subscribers"]
    )
def subscribe(
    email: EmailStr = Form(...), 
    user_agent: Optional[str] = Header(default=None)
    ):
    return user_agent 