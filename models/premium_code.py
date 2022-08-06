
from datetime import datetime

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta

premium_codes = Table('premium_codes', meta,
    Column('premium_cod', String(36), primary_key=True),
    Column('user_id', Integer(), foreign_key=True, nullable=True),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime)
    )