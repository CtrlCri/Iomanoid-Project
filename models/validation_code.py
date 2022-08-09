# Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import DateTime, Integer, String, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship

# Local
from config.db import Base

class ValidationCode(Base):
    __tablename__ = "validation_codes"

    code = Column(String(36), primary_key=True)
    #user_id = Column(Integer(), ForeignKey("users.user_id") nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)