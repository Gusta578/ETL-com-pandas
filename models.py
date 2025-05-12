from database import Base
from sqlalchemy import Column, Boolean, String, Integer, Date
from database import engine, Base

class Funcionarios(Base):
    __tablename__ = "funcionarios_ativos"

    id = Column(Integer, nullable=False, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(Date)
    salario = Column(Integer)
    ativo = Column(Boolean)
    idade = Column(Integer)

Base.metadata.create_all(engine)

