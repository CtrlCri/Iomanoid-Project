
from sqlalchemy import INTEGER, VARCHAR, DATETIME, Table, Column
from config.db import meta

users = Table(
    'users', meta,
    Column('id', INTEGER),
    Column('email', VARCHAR(50)),
    Column('user_name', VARCHAR(50),
    Column('created_at', DATETIME),
    Column('updated_at', DATETIME)
)