# Python
from datetime import datetime

# SQLAlchemy
from sqlalchemy import DateTime, Integer, String, Boolean, Column
#from sqlalchemy.orm import relationship

# Local
from config.db import Base

class Subscriber(Base):
    __table__ = "subscribers"

    subscriber_id = Column(Integer(), primary_key=True)
    email = Column(String(45), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)
    