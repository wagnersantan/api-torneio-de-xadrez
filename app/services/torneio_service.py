from sqlalchemy.orm import Session
from app.repositories.torneio_repository import TorneioRepository
from app.models.torneio_model_sqlalchemy import Torneio
from app.schemas.torneio_schema import TorneioCreate
from typing import List, Optional

class TorneioService:
    def __init__(self, db: Session):
        self.repository = TorneioRepository(db)

    def criar_torneio(self, torneio_create: TorneioCreate) -> Torneio:
        # Converte o Pydantic para o modelo SQLAlchemy
        novo_torneio = Torneio(
            nome=torneio_create.nome,
            status=torneio_create.status,
            data_inicio=torneio_create.data_inicio,
            data_fim=torneio_create.data_fim,
            local=torneio_create.local
        )
        return self.repository.salvar(novo_torneio)

    def listar_torneios(self) -> List[Torneio]:
        return self.repository.listar_todos()

    def buscar_torneio_por_id(self, torneio_id: int) -> Optional[Torneio]:
        return self.repository.buscar_por_id(torneio_id)

    def atualizar_torneio(self, torneio_id: int, dados_atualizados: dict) -> Optional[Torneio]:
        return self.repository.atualizar(torneio_id, dados_atualizados)

    def deletar_torneio(self, torneio_id: int) -> bool:
        return self.repository.deletar(torneio_id)
