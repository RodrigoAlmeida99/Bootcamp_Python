from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///DB.db', echo=True)
Base = declarative_base()

class Usuario(Base): 
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(length=50))
    idade = Column(Integer)

Base.metadata.create_all(engine)