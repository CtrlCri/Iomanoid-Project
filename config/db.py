from sqlalchemy import create_engine
from sqlalchemy import MetaData

#DATABASE_URL = "mysql+pymysql://root@localhost:3306/iomanoid"

engine = create_engine('mysql+pymysql://root@localhost:3306/test')
meta = MetaData()
conn = engine.connect()