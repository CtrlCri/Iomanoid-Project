
from datetime import datetime

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta

validation_codes = Table('validation_codes', meta,
    Column('validation_cod', String(36), primary_key=True),
    Column('project_id', Integer(), foreign_key=True, nullable=True),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime)
    )