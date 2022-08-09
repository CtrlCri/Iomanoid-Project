#Python
from typing import Optional, List
from datetime import datetime
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field, EmailStr, HttpUrl

# Local
#from schemas.user import User


# Models

class Marketplace(Enum):
    opensea = "OpenSea"
    rarible = "Rarible"
    otro = "Otro"

class Blockchain(Enum):
    polygon = "Polygon"
    ethereum = "Ethereum"
    solana = "Solana"

class Tags(Enum):
    art = "Art"
    collectible = "Collectible"
    dao = "DAO"
    game = "Game"
    metaverse = "Metaverse"

class Project(BaseModel):
    project_name: str = Field(..., min_length=1, max_length=50, example="Iomis of Metaverse")
    #image_file: UploadFile = File(...)
    blockchain: Blockchain = Field(...)
    marketplace: Optional[Marketplace] = Field()
    
    collection_size: int = Field(..., gt=0, lt=22223, example=1119)
    description: str = Field(..., max_length=500, min_length=50,
    example="""Estos son los Iomis del Metaverso; su principal funcionalidad es la de proveer 
    privilegios excusivos sobre la plataforma Iomanoid.io a quien los posea; 
    por ejemplo: Acceso premium a funcionalidades tales como -listar/editar más de un proyecto. 
    Porque calaveras/esqueletos... toda la info en nuestro sitio web: Iomanoids.com""")
    release_date: Optional[datetime] = Field(default=None) # NFT drop
    instagram: Optional[HttpUrl] = Field(example="https://instagram.com/iomanoid_nfts")
    twitter: Optional[HttpUrl] = Field(example="https://twitter.com/iomanoid_nfts")
    discord: Optional[HttpUrl] = Field(example="https://discord.com/")
    website: Optional[HttpUrl] = Field(example="https://iomanoids.com")
    source: Optional[HttpUrl] = Field(example="https://www.github.com/armycrih")
    marketplace_url: Optional[HttpUrl] = Field(example="https://www.opensea.com/collection/iomanoid-genesis")

    tags: Optional[Tags] = Field()
    created_date: datetime = Field(default=datetime.now())
    updated_date: Optional[datetime] = Field(default=None)
    
    #owner_id: Optional[User] = Field(default=None)

    class Config:
        orm_mode = True



