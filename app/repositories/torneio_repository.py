from sqlalchemy.orm import Session
from app.models.torneio_model_sqlalchemy import Torneio
from typing import Optional, List

class TorneioRepository:
    def __init__(self, db: Session):
        self.db = db

    def salvar(self, torneio: Torneio) -> Torneio:
        self.db.add(torneio)
        self.db.commit()
        self.db.refresh(torneio)
        return torneio

    def listar_todos(self) -> List[Torneio]:
        return self.db.query(Torneio).all()

    def buscar_por_id(self, torneio_id: int) -> Optional[Torneio]:
        return self.db.query(Torneio).filter(Torneio.id == torneio_id).first()

    def atualizar(self, torneio_id: int, dados_atualizados: dict) -> Optional[Torneio]:
        torneio = self.buscar_por_id(torneio_id)
        if not torneio:
            return None
        for chave, valor in dados_atualizados.items():
            setattr(torneio, chave, valor)
        self.db.commit()
        self.db.refresh(torneio)
        return torneio

    def deletar(self, torneio_id: int) -> bool:
        torneio = self.buscar_por_id(torneio_id)
        if not torneio:
            return False
        self.db.delete(torneio)
        self.db.commit()
        return True

