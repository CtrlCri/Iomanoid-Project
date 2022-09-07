# Python
from typing import List
from os import getcwd # for images

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path
from fastapi import Depends, HTTPException
from fastapi import File, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse

# SQLAlchemy
from sqlalchemy.orm import Session

#
from werkzeug.security import generate_password_hash, check_password_hash
from PIL import Image

# Local
from config.db import SessionLocal,Base, engine
from models import User as UserModel
from models import Project as ProjectModel
from schemas import Blockchain, User as UserSchema, SignUp, UserUpdate
from schemas import Project as ProjectSchema, ProjectUpdate
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
    return db.query(UserModel).all()

### Register a user
@user.post(
    path="/users/signup",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(db: Session=Depends(get_db), user: SignUp=Body(...)):
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
    path="/projects/",
    response_model=List[ProjectSchema],
    status_code=status.HTTP_200_OK,
    summary="Show all projects",
    tags=["Projects"]
)
def get_users(db: Session=Depends(get_db)): 
    return db.query(ProjectModel).all()

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
        owner_id = project.owner_id,
        blockchain = project.blockchain.value,
        marketplace = project.marketplace.value,
        marketplace_url = project.marketplace_url,
        collection_size= project.collection_size,
        release_date = project.release_date,
        instagram = project.instagram,
        twitter = project.twitter,
        discord = project.discord,
        website = project.website,
        source = project.source,
        created_at = project.created_at,
        updated_at = project.updated_at 
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
   
    return new_project

PATH_IMAGES = getcwd() + "/images/"

def resize_image(filename: str):
    sizes = [
        {"width": 1280, "heigth": 720},
        {"width": 640, "heigth": 480}
    ]
    for size in sizes:
        size_defined = size["width"], size["heigth"]
        image = Image.open(PATH_IMAGES + filename, mode="r")
        image.thumbnail(size_defined)
        image.save(PATH_IMAGES + str(size["heigth"]) + "_" + filename)
    print("success")

@project.post(
    path="/project/image",
    status_code=status.HTTP_200_OK,
    summary="Upload a Project Image",
    tags=["Projects"]
)
async def project_image(backgraund_task: BackgroundTasks, image: UploadFile = File(...)):
    # SAVE FILE ORIGINAL
    with open( PATH_IMAGES + image.filename, "wb") as myfile:
        content = await image.read()
        myfile.write(content)
        myfile.close()
    
    # RESIZE IMAGES
    backgraund_task.add_task(resize_image, filename=image.filename)
    return JSONResponse(content={"message": "success"})

### Update a project
@project.put(
    path="/projects/{id}",
    response_model=ProjectSchema,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Update a Project",
    tags=["Projects"]
)
def update_project(db: Session=Depends(get_db), id: int=Path(...), project: ProjectUpdate=Body(...)): 
    data_project = db.query(ProjectModel).filter_by(project_id=id).first()
    data_project.project_name = project.project_name,
    data_project.email = project.description
    db.commit()
    db.refresh(data_project)
    return data_project

### Delete a project
@project.delete(
    path="/projects/{id}",
    response_model=SchemaReply,
    status_code=status.HTTP_200_OK,
    summary="Delete a Project",
    tags=["Projects"]
)   
def delete_project(id: int=Path(...), db: Session=Depends(get_db)): 
    project = db.query(ProjectModel).filter_by(project_id=id).first()
    db.delete(project)
    db.commit()
    message = SchemaReply(message="Successeful deleted")
    return message