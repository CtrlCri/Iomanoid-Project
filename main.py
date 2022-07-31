# Python
from datetime import date, datetime
from typing import Optional, List
from enum import Enum
from uuid import UUID

# Pydantic
from pydantic import BaseModel
from pydantic import Field 
from pydantic import EmailStr, HttpUrl 

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File

app = FastAPI()

# Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )

class User(UserBase):
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=20
    )
    created_date: datetime = Field(default=datetime.now())
    updated_date: Optional[datetime] = Field(default=None)
    

class Marketplace(Enum):
    opensea = "OpenSea"
    rarible = "Rarible"
    otro = "Otro"

class Blockchain(Enum):
    polygon = "Polygon"
    ethereum = "Ethereum"
    solana = "Solana"

class ProjectBase(BaseModel):
    project_id: UUID = Field(...)
    project_name: str = Field(..., min_length=1, max_length=50, example="Iomis of Metaverse")
    #image_file: UploadFile = File(...)
    blockchain: Blockchain = Field(...)
    marketplace: Optional[Marketplace] = Field(default=None)
    
    collection_size: int = Field(..., gt=0, lt=22223, example=1119)
    description: str = Field(..., max_length=500, min_length=50,
    example="""Estos son los Iomis del Metaverso; su principal funcionalidad es la de proveer 
    privilegios excusivos sobre la plataforma Iomanoid.io a quien los posea; 
    por ejemplo: Acceso premium a funcionalidades tales como -listar/editar más de un proyecto. 
    Porque calaveras/esqueletos... toda la info en nuestro sitio web: Iomanoids.com""")
    release_date: Optional[date] = Field(default=None) # NFT drop
    instagram: Optional[HttpUrl] = Field(example="https://instagram.com/iomanoid_nfts")
    twitter: Optional[HttpUrl] = Field(example="https://twitter.com/iomanoid_nfts")
    discord: Optional[HttpUrl] = Field(example="https://discord.com/")
    website: Optional[HttpUrl] = Field(example="https://iomanoids.com")
    source: Optional[HttpUrl] = Field(example="https://www.github.com/armycrih")
    marketplace_url: Optional[HttpUrl] = Field(example="https://www.opensea.com/collection/iomanoid-genesis")

    created_date: datetime = Field(default=datetime.now())
    updated_date: Optional[datetime] = Field(default=None)

class Project(ProjectBase):
    
    secret_code: str = Field(..., example="ARMYCRIHARMYCRIH")
    #tags: list

class ProjectOut(ProjectBase):
    pass

# Path Operations

### Home
@app.get(
    path="/", 
    status_code=status.HTTP_200_OK,
    tags=["Home"]
    )
def home():
    return {"Iomanoid": "Génesis"}

## Users

### Register a user
@app.post(
    path="/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(): 
    pass

### Login a user
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login(): 
    pass

### Show all users
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users(): 
    pass

### Show a user
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"]
)
def show_a_user(): 
    pass

### Delete a user
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"]
)
def delete_a_user(): 
    pass

### Update a user
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_a_user(): 
    pass

## Projects

### Register project

@app.post(
    path="/project/new/", 
    response_model=ProjectOut, 
    status_code=status.HTTP_201_CREATED,
    tags=["Projects"],
    summary="Publish a project in the app"
    )
def publish_project(project: Project = Body(...)):
    """
    Publish Project

    This path operation post a project in the app and save the information in the database

    Parameters: 
    - Request body parameter: 
        - **project: Project** -> A project model with name, blockchain, marketplace, size, description, release date, website and RRSS

    Returns a project model with name, blockchain, marketplace, size, description, release date, website and RRSS
    """
    return project

### Show a project

@app.get(
    path="/project/detail/{project_id}",
    status_code=status.HTTP_200_OK,
    tags=["Projects"],
    summary="Show a Project"
    )
def show_project(
    project_id: int = Path(
        ..., 
        gt=0,
        title="Project ID",
        description="This is de Project ID, it´s required"
        )
):
    """
    Show a Project

    This path operation show a project in the database

    Parameters: 
    - Path parameter: 
        - **project id: int** -> A project identifier

    Returns confirmation of whether the project exists in the database or not
    """
    pass

### Update a project

@app.put(
    path="/project/{project_id}", 
    response_model=ProjectOut, 
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Projects"]
    )
def update_project(
    project_id: int = Path(
        ...,
        title="Project ID",
        description="This is the Project ID",
        gt=0
    ),
    project: Project = Body(...)
    ):
    return project  

## Subscribers
### 

@app.post(
    path="/subscribe", 
    status_code=status.HTTP_200_OK,
    tags=["Subscribers"]
    )
def subscribe(
    email: EmailStr = Form(...), 
    user_agent: Optional[str] = Header(default=None)
    ):
    return user_agent 