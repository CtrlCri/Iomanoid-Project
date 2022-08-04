
from sqlalchemy import Integer, String, Table, Column
from config.db import meta
#from sqlalchemy import MetaData
users = Table('users', meta,
    Column('id', Integer, primary_key=True),
    Column('email', String(50)),
    Column('user_name', String(50)),
    Column('created_at', String),
    Column('updated_at', String)
    )
