#Python
from email import message
from typing import Optional, List
from datetime import datetime
from enum import Enum
from uuid import UUID

# Pydantic
from pydantic import BaseModel, Field, EmailStr

# Local
#from project import Project as SchemaProject

# Project
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
    project_id: int
    project_name: str = Field(..., min_length=1, max_length=50, example="Iomis of Metaverse")
    #image_file: UploadFile = File(...)
    #blockchain: Blockchain = Field(...)
    #marketplace: Optional[Marketplace] = Field()
    
    #collection_size: int = Field(..., gt=0, lt=22223, example=1119)
    description: str = Field(..., max_length=500, min_length=50)
    owner_id: Optional[int] = Field(default=None)
    #release_date: Optional[datetime] = Field(default=None) # NFT drop
    #instagram: Optional[HttpUrl] = Field(example="https://instagram.com/iomanoid_nfts")
    #twitter: Optional[HttpUrl] = Field(example="https://twitter.com/iomanoid_nfts")
    #discord: Optional[HttpUrl] = Field(example="https://discord.com/")
    #website: Optional[HttpUrl] = Field(example="https://iomanoids.com")
    #source: Optional[HttpUrl] = Field(example="https://www.github.com/armycrih")
    #marketplace_url: Optional[HttpUrl] = Field(example="https://www.opensea.com/collection/iomanoid-genesis")

    #tags: Optional[Tags] = Field()
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)

    class Config:
        orm_mode = True


# User
class UserBase(BaseModel):
    user_id: Optional[int]
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=45
    )
    email: EmailStr = Field(...)
    password: str = Field(...)

class User(UserBase):
    #is_active: bool = Field(..., default=True)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)  
    
    projects: List[Project] = []

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    user_name: str = Field(
        ...,
        min_length=5,
        max_length=45
    )
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(...)

class Reply(BaseModel):
    message: str

# Subscriber
class Subscriber(BaseModel):
    email: EmailStr = Field(...)
    created_at: datetime = Field(default=datetime.now())

# ValidationCode
class ValidationCode(BaseModel):
    code: UUID = Field(...)
    enabled: bool = Field(default=False)

# PremiumCode
class PremiumCode(BaseModel):
    code: UUID = Field(...)
    enabled: bool = Field(default=False)
