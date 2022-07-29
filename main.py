#Python
from datetime import date
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field 
from pydantic import HttpUrl, FilePath

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models
class Marketplace(Enum):
    opensea = "OpenSea"
    rarible = "Rarible"
    otro = "Otro"

class Blockchain(Enum):
    polygon = "Polygon"
    ethereum = "Ethereum"
    solana = "Solana"

class Project(BaseModel):
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

    #tags: list


@app.post("/project/new/")
def create_project(project: Project = Body(...)):
    return project

@app.get("/project/detail/{project_id}")
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

@app.put("/project/{project_id}")
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
