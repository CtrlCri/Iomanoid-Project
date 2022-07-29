#Python
from datetime import date
from email import message
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field 
from pydantic import HttpUrl, FilePath, EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Header
from fastapi import status

app = FastAPI()

# Models
class LoginOut(BaseModel):
    message: str = Field(default="Login successfully")

class Marketplace(Enum):
    opensea = "OpenSea"
    rarible = "Rarible"
    otro = "Otro"

class Blockchain(Enum):
    polygon = "Polygon"
    ethereum = "Ethereum"
    solana = "Solana"

class ProjectBase(BaseModel):
    project_name: str = Field(..., min_length=1, max_length=50, example="Iomis of Metaverse")
    image: FilePath = Field(..., example="C:/Users/Crih/Pictures/iomanoid.png")
    release_date: Optional[date] = Field(default=None) # NFT drop
    marketplace: Optional[Marketplace] = Field(default=None)
    blockchain: Blockchain = Field(...)
    collection_size: int = Field(..., gt=0, lt=22223, example=1119)
    description: str = Field(..., max_length=500, min_length=50,
    example="""Estos son los Iomis del Metaverso; su principal funcionalidad es la de proveer 
    privilegios excusivos sobre la plataforma Iomanoid.io a quien los posea; 
    por ejemplo: Acceso premium a funcionalidades tales como -listar/editar más de un proyecto. 
    Porque calaveras/esqueletos... toda la info en nuestro sitio web: Iomanoids.com""")

    instagram: Optional[HttpUrl] = Field(example="https://instagram.com/iomanoid_nfts")
    twitter: Optional[HttpUrl] = Field(example="https://twitter.com/iomanoid_nfts")
    discord: Optional[HttpUrl] = Field(example="https://discord.com/")
    website: Optional[HttpUrl] = Field(example="https://iomanoids.com")
    source: Optional[HttpUrl] = Field(example="https://www.github.com/armycrih")
    marketplace_url: Optional[HttpUrl] = Field(example="https://www.opensea.com/collection/iomanoid-genesis")

class Project(ProjectBase):
    
    secret_code: str = Field(..., example="ARMYCRIHARMYCRIH")
    #tags: list

class ProjectOut(ProjectBase):
    pass

@app.get(path="/", status_code=status.HTTP_200_OK)
def home():
    return {"Iomanoid": "Génesis"}

@app.post(path="/project/new/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(project: Project = Body(...)):
    return project

@app.get(path="/project/detail/{project_id}", status_code=status.HTTP_200_OK)
def show_project(
    project_id: int = Path(
        ..., 
        gt=0,
        title="Project ID",
        description="This is de Project ID, it´s required"
        )
):
    return {
        "Project ID": project_id
        }

@app.put(path="/project/{project_id}", response_model=ProjectOut, status_code=status.HTTP_202_ACCEPTED)
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

@app.post(path="/login", response_model=LoginOut, status_code=status.HTTP_200_OK)
def login(secret_code: str = Form(...)):
    return LoginOut()

@app.post(path="/subscribe", status_code=status.HTTP_200_OK)
def subscribe(
    email: EmailStr = Form(...), 
    user_agent: Optional[str] = Header(default=None)
    ):
    return user_agent 