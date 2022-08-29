# Python
from datetime import datetime

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
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    projects = relationship("Project", back_populates="owner")
    
    __table_args__= {
        'mysql_engine':'InnoDB'
    }



class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer(), primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False, unique=True)
    description = Column(String(450), nullable=False)
    owner_id = Column(Integer(), ForeignKey("users.user_id"), nullable=True)

    blockchain = Column(Enum('Polygon', 'Ethereum', 'Solana', 'Otro'))
    marketplace = Column(Enum('OpenSea', 'Rarible', 'Otro', 'En proceso'))
    collection_size = Column(Integer(), nullable=False)
    release_date = Column(DateTime) 
    
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    
    owner = relationship("User", back_populates="projects")

    __table_args__= {
        'mysql_engine':'InnoDB'
    }


class Subscriber(Base):
    __tablename__ = "subscribers"

    subscriber_id = Column(Integer(), primary_key=True)
    email = Column(String(45), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    
class ValidationCode(Base):
    __tablename__ = "validation_codes"

    code = Column(String(36), primary_key=True)
    #user_id = Column(Integer(), ForeignKey("users.user_id") nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

class PremiumCode(Base):
    __tablename__ = "premium_codes"

    code = Column(String(36), primary_key=True)
    #user_id = Column(Integer(), ForeignKey("users.user_id") nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)




