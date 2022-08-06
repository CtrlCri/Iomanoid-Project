
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Table, Column
from config.db import meta

subscribers = Table('subscribers', meta,
    Column('subscriber_id', Integer(), primary_key=True),
    Column('email', String(45), nullable=False, unique=True),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime)
    )
