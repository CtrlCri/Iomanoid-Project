
from sqlalchemy import DateTime, Integer, String, Table, Column
from config.db import meta
#from sqlalchemy import MetaData
users = Table('users', meta,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(45)),
    Column('email', String(45)),
    Column('created_at', DateTime),
    Column('updated_at', DateTime)
    )
