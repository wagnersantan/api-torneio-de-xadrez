import enum
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum as SqlEnum
from app.database.connection import Base

class StatusTorneioEnum(str, enum.Enum):
    ABERTO = "aberto"
    ENCERRADO = "encerrado"
    EM_ANDAMENTO = "em_andamento"

class Torneio(Base):
    __tablename__ = "torneios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    status = Column(SqlEnum(StatusTorneioEnum), nullable=False)
    data_inicio = Column(DateTime, nullable=False)
    data_fim = Column(DateTime, nullable=False)
    local = Column(String, nullable=False)
