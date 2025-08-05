# app/services/torneio_service.py

from app.repositories.torneio_repository import TorneioRepository
from app.models.torneio_model import TorneioModel
from typing import List, Optional

class TorneioService:
    def __init__(self):
        self.repository = TorneioRepository()

    def criar_torneio(self, torneio: TorneioModel) -> TorneioModel:
        # Aqui poderia ter lógica adicional de negócio antes de salvar
        return self.repository.salvar(torneio)

    def listar_torneios(self) -> List[TorneioModel]:
        return self.repository.listar_todos()

    def buscar_torneio_por_id(self, torneio_id: str) -> Optional[TorneioModel]:
        return self.repository.buscar_por_id(torneio_id)

    def atualizar_torneio(self, torneio_id: str, dados_atualizados: dict) -> Optional[TorneioModel]:
        # Poderia validar dados antes de atualizar
        return self.repository.atualizar(torneio_id, dados_atualizados)

    def deletar_torneio(self, torneio_id: str) -> bool:
        return self.repository.deletar(torneio_id)
