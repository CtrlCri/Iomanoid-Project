# Python from uuid import UUID
from typing import List

# Pydantic from pydantic import HttpUrl

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path

#
from models.user import users
from config.db import conn
from schemas.index import User, UserUpdate


user = APIRouter()


## Users

### Show all users
@user.get(
    path="/",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def read_data(): 
    return conn.execute(users.select()).fetchall()

### Show a user
@user.get(
    path="/{id}",
    #response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def read_data(id: int=Path(...)): 
    return conn.execute(users.select().where(users.c.user_id == id)).fetchall()

### Register a user
@user.post(
    path="/signup",
    #response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def write_data(user: User=Body(...)):
    conn.execute(users.insert().values(
        user_name = user.user_name,
        email = user.email,
        created_at = user.created_at,
        updated_at = user.updated_at
    )) 
    return conn.execute(users.select()).fetchall()

### Update a user
@user.put(
    path="/{id}/update",
    #response_model=User,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a User",
    tags=["Users"]
)
def update_data(id: int=Path(...), user: UserUpdate=Body(...)): 
    conn.execute( users.update().values(
        user_name = user.user_name,
        email = user.email
    ).where(users.c.user_id == id)) 
    return conn.execute(users.select()).fetchall()

### Delete a user
@user.delete(
    path="/{id}/delete",
    #response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_data(id: int): 
    conn.execute(users.delete().where(users.c.user_id == id ))
    return conn.execute(users.select()).fetchall()

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

