# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path
from fastapi import Depends, HTTPException

# SQLAlchemy
from sqlalchemy.orm import Session

# Local
from config.db import SessionLocal
from models.user import User as ModelUser
from schemas.user import User as SchemaUser, UserUpdate



user = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

### Show all users
@user.get(
    path="/users/",
    response_model=List[SchemaUser],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def get_users(db: Session=Depends(get_db)): 
    return db.query(ModelUser).all()

### Show a user
@user.get(
    path="/{id}",
    #response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def read_data(id: int=Path(...)): 
    pass #conn.execute(users.select().where(users.c.user_id == id)).fetchall()

### Register a user
@user.post(
    path="/signup",
    #response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def write_data(user: SchemaUser=Body(...)):
    #conn.execute(users.insert().values(
    #    user_name = user.user_name,
    #    email = user.email,
    #    created_at = user.created_at,
    #    updated_at = user.updated_at
    #)) 
    pass

### Update a user
@user.put(
    path="/{id}/update",
    #response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a User",
    tags=["Users"]
)
def update_data(id: int=Path(...), user: UserUpdate=Body(...)): 
    #conn.execute( users.update().values(
    #    user_name = user.user_name,
    #    email = user.email
    #).where(users.c.user_id == id)) 
    pass

### Delete a user
@user.delete(
    path="/{id}/delete",
    #response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_data(id: int): 
    #conn.execute(users.delete().where(users.c.user_id == id ))
    pass

### Login a user
#@user.post(
#    path="/login",
#    response_model=User,
#    status_code=status.HTTP_200_OK,
#    summary="Login a User",
#    tags=["Users"]
#)
# def login(): 
#    pass

