
from datetime import datetime
from uuid import UUID

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta, engine

premium_codes = Table('premium_codes', meta,
    Column('code', String(36), primary_key=True),
    Column('user_id', Integer(), nullable=True),
    Column('created_at', DateTime, nullable=False, default=datetime.now()),
    Column('updated_at', DateTime)
    )

meta.create_all(engine)