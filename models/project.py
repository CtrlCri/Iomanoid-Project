
from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Table, Column
from config.db import meta

projects = Table('projects', meta,
    Column('project_id', Integer(), primary_key=True),
    Column('project_name', String(45), nullable=False, unique=True),
    Column('descripcion', String(450), nullable=False),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime)
    )

