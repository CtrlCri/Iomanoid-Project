
from datetime import datetime
from models.user import users

from sqlalchemy import Table, Column, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import DateTime, Integer, String 
from config.db import meta, engine



projects = Table('projects', meta,
    Column('project_id', Integer(), 
        primary_key=True, autoincrement=True),
    Column('project_name', String(45), nullable=False, unique=True),
    Column('descripcion', String(450), nullable=False),
    #Column('user_id', Integer(), foreign_key=True),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime)
    )

meta.create_all(engine)


