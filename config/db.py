from sqlalchemy import create_engine
from sqlalchemy import MetaData

DATABASE_URL = "mysql+pymysql://root:toor@localhost:3306/iomanoid"

engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()