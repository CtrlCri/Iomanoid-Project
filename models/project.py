# Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import DateTime, Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship

# Local
from config.db import Base

class Project(Base):
    __tablename__ = "projects"
    project_id = Column(Integer(), primary_key=True, autoincrement=True),
    project_name = Column(String(45), nullable=False, unique=True),
    descripcion = Column(String(450), nullable=False),
    owner_id = Column(Integer(), ForeignKey("users.user_id")),
    created_at = Column(DateTime, default=datetime.now()),
    updated_at = Column(DateTime)
    
    owner = relationship("User", back_populates="projects")

    __table_args__= {
        'mysql_engine':'InnoDB'
    }


