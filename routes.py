# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path
from fastapi import Depends, HTTPException

# SQLAlchemy
from sqlalchemy.orm import Session

#
from werkzeug.security import generate_password_hash, check_password_hash

# Local
from config.db import SessionLocal
from models import User as ModelUser
from models import Project as ModelProject
from schemas import User as SchemaUser, UserUpdate
from schemas import Project as SchemaProject
from schemas import Reply as SchemaReply



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
    #users = db.query(ModelUser).all()
    return db.query(ModelUser).all()

### Show a user
@user.get(
    path="/users/{id}",
    response_model=SchemaUser,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def read_data(id: int=Path(...), db: Session=Depends(get_db)): 
    user = db.query(ModelUser).filter_by(user_id=id).first()
    return user  

### Register a user
@user.post(
    path="/users/signup",
    response_model=SchemaUser,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(db: Session=Depends(get_db), user: SchemaUser=Body(...)):
    new_user = ModelUser(
        user_name = user.user_name,
        email = user.email,
        password = user.password
    )
    #new_user["password"] = generate_password_hash(user.password, "pbkdf2:sha256:10")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

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
    response_model=SchemaReply,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)   
def delete_user(id: int=Path(...), db: Session=Depends(get_db)): 
    user = db.query(ModelUser).filter_by(user_id=id).first()
    db.delete(user)
    db.commit()
    message = SchemaReply(message="Successeful deleted")
    return message
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

## Subscribers
### 

### Register a project
@user.post(
    path="/project/new",
    response_model=SchemaProject,
    status_code=status.HTTP_201_CREATED,
    summary="Register a Project",
    tags=["Projects"]
)
def signup(db: Session=Depends(get_db), project: SchemaProject=Body(...)):
    db_project = ModelProject(
        project_name = project.project_name,
        description = project.description,
        created_at = project.created_at,
        updated_at = project.updated_at 
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project