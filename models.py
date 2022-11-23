# Python
from datetime import datetime
from enum import unique

# SQLAlchemy
from sqlalchemy import ForeignKey, DateTime, Integer, String, Boolean, Column, Enum
from sqlalchemy.orm import relationship

# Local
from config.db import Base


class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(300))
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    projects = relationship("Project", back_populates="owner")
    code = relationship("PremiumCode", back_populates="user")
       
    def __str__(self):
        return self.user_name
        



class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer(), primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False, unique=True)
    description = Column(String(450), nullable=False)
    owner_id = Column(Integer(), ForeignKey("users.user_id"), nullable=True)

    blockchain = Column(Enum('Polygon', 'Ethereum', 'Solana', 'Otro', name="blockchain"))
    marketplace = Column(Enum('OpenSea', 'Rarible', 'Otro', 'En proceso', name="marketplace"))
    marketplace_url = Column(String(300), nullable=True)
    collection_size = Column(Integer(), nullable=False)

    release_date = Column(DateTime, nullable=True) 
    
    instagram = Column(String(70), nullable=True)
    twitter = Column(String(70), nullable=True)
    discord = Column(String(70), nullable=True)
    website = Column(String(70), nullable=True)

    tags = Column(String(70), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, nullable=True) 
    
    owner = relationship("User", back_populates="projects")
    code = relationship("ValidationCode", back_populates="project")

    
    def __str__(self):
        return self.project_name


class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    email = Column(String(45), nullable=False, unique=True)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    
class ValidationCode(Base):
    __tablename__ = "validation_codes"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    code = Column(String(36), unique=True)
    enabled = Column(Boolean, default=True)
    project_id = Column(Integer(), ForeignKey("projects.project_id"), nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    project = relationship("Project", back_populates="code")


class PremiumCode(Base):
    __tablename__ = "premium_codes"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    code = Column(String(36), unique=True)
    enabled = Column(Boolean, default=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"), nullable=True)
    
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="code")





