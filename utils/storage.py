from sqlalchemy import create_engine, Integer, String, Float, Column
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


engine = create_engine('sqlite:///mydatabase_orm.db', echo=True)

Base = declarative_base()
