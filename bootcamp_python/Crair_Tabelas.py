from sqlalchemy import create_engine , Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///DB.db', echo=True)
base = declarative_base()


class Fornecedor(base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(base): 
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    Fornecedor = relationship('Fornecedor')


base.metadata. create_all(engine)

Session  = sessionmaker(bind=engine)
session = Session()

try: 
    with Session() as session: 
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='12345678', email= 'abcd@gmail.com', endereco='rua abc'),
            Fornecedor(nome='Fornecedor B', telefone='87654321', email= 'cba@gmail.com', endereco='rua cba')
        ]
        session.add_all(fornecedores)
        session.commit()
except e:
    print("Erro na extri dos dados - Fornecedor")


try: 
    with Session() as session: 
        fornecedores = [
            Produto(nome='produto A', descricao='produto de ...', preco= '15'),
            Produto(nome='produto B', descricao='produto para ...', preco= '20')
        ]
        session.add_all(fornecedores)
        session.commit()
except e: 
    print("Erro na extri dos dados - Produto")