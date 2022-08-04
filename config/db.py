from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysqlconnector://root@localhost:3306/iomanoid"

engine = create_engine(DATABASE_URL)
meta = MetaData
conn = engine.connect()