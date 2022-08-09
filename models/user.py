
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer(), primary_key=True, autoincrement=True),
    user_name = Column(String(45), nullable=False, unique=True),
    email = Column(String(45), nullable=False, unique=True),
    password = Column(String(25)),
    is_active = Column(Boolean, default=True),
    created_at = Column(DateTime, nullable=False, default=datetime.now()),
    updated_at = Column(DateTime)

    projects = relationship("Project", back_populates="owner")
    
    __table_args__= {
        'mysql_engine':'InnoDB'
    }
