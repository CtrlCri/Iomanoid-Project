
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Table, Column
from config.db import meta, engine

users = Table('users', meta,
    Column('user_id', Integer(),
        primary_key=True, autoincrement=True),
    Column('user_name', String(45), nullable=False, unique=True),
    Column('email', String(45), nullable=False, unique=True),
    Column('created_at', DateTime, nullable=False, default=datetime.now()),
    Column('updated_at', DateTime)
    )

meta.create_all(engine)