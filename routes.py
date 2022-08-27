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
from config.db import SessionLocal,Base, engine
from models import User as UserModel
from models import Project as ProjectModel
from schemas import User as UserSchema, UserUpdate
from schemas import Project as ProjectSchema
from schemas import Reply as SchemaReply

Base.metadata.create_all(bind=engine) 

user = APIRouter()
project = APIRouter()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

### Show all users
@user.get(
    path="/users/",
    response_model=List[UserSchema],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def get_users(db: Session=Depends(get_db)): 
    #users = db.query(UserModel).all()
    return db.query(UserModel).all()

### Register a user
@user.post(
    path="/users/signup",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(db: Session=Depends(get_db), user: UserSchema=Body(...)):
    hash_password = generate_password_hash(user.password, method='pbkdf2:sha256')
    new_user = UserModel(
        user_name = user.user_name,
        email = user.email,
        password = hash_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
   
    return new_user

### Show a user
@user.get(
    path="/users/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def read_data(id: int=Path(...), db: Session=Depends(get_db)): 
    user = db.query(UserModel).filter_by(user_id=id).first()
    return user  


### Update a user
@user.put(
    path="/users/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a User",
    tags=["Users"]
)
def update_user(db: Session=Depends(get_db), id: int=Path(...), user: UserUpdate=Body(...)): 
    data_user = db.query(UserModel).filter_by(user_id=id).first()
    data_user.user_name = user.user_name,
    data_user.email = user.email
    db.commit()
    db.refresh(data_user)
    return data_user

### Delete a user
@user.delete(
    path="/users/{id}",
    response_model=SchemaReply,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)   
def delete_user(id: int=Path(...), db: Session=Depends(get_db)): 
    user = db.query(UserModel).filter_by(user_id=id).first()
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


### Show all projects
@project.get(
    path="/users/",
    response_model=List[UserSchema],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Projects"]
)
def get_users(db: Session=Depends(get_db)): 
    #users = db.query(UserModel).all()
    return db.query(UserModel).all()

### Post a project
@project.post(
    path="/project/new",
    response_model=ProjectSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Project",
    tags=["Projects"]
)
def post_project(db: Session=Depends(get_db), project: ProjectSchema=Body(...)):
    new_project = ProjectModel(
        project_name = project.project_name,
        description = project.description,
        created_at = project.created_at,
        updated_at = project.updated_at 
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
   
    return new_project

### Update a project
@project.put(
    path="/projects/{id}",
    response_model=UserSchema,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a User",
    tags=["Projects"]
)
def update_project(db: Session=Depends(get_db), id: int=Path(...), user: UserUpdate=Body(...)): 
    data_user = db.query(UserModel).filter_by(user_id=id).first()
    data_user.user_name = user.user_name,
    data_user.email = user.email
    db.commit()
    db.refresh(data_user)
    return data_user

### Delete a project
@project.delete(
    path="/projects/{id}",
    response_model=SchemaReply,
    status_code=status.HTTP_200_OK,
    summary="Delete a Project",
    tags=["Projects"]
)   
def delete_project(id: int=Path(...), db: Session=Depends(get_db)): 
    user = db.query(UserModel).filter_by(user_id=id).first()
    db.delete(user)
    db.commit()
    message = SchemaReply(message="Successeful deleted")
    return message