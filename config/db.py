# SQLAlchemy
from sqlalchemy import create_engine
#from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:toor@localhost:3306/iomanoid"
engine = create_engine(DATABASE_URL)
#meta = MetaData()
Base = declarative_base()
#conn = engine.connect()