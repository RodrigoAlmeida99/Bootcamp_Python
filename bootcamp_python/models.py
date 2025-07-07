from sqlalchemy import create_engine , Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///DB.db', echo=True)
base = declarative_base()


class Item(base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, index=Treu)
    nome = Column(String(50), inder=False)
    price = Column(float)
    is_offer = Column(String, nullable=True)



base.metadata. create_all(engine)

