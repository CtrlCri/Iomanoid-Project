
from datetime import datetime

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from config.db import meta, engine

validation_codes = Table('validation_codes', meta,
    Column('code', String(36), primary_key=True),
    Column('project_id', Integer(), nullable=True),
    Column('created_at', DateTime, nullable=False, default=datetime.now()),
    Column('updated_at', DateTime)
    )

meta.create_all(engine)
