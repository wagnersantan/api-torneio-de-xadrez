from typing import List
from app.models.enxadrista_model import EnxadristaModel
from app.schemas.enxadrista_schema import EnxadristaCreate, EnxadristaUpdate
from app.repositories.enxadrista_repository import EnxadristaRepository

class EnxadristaService:
    def __init__(self, repository: EnxadristaRepository):
        self.repository = repository

    def listar_enxadristas(self) -> List[EnxadristaModel]:
        return self.repository.listar_todos()

    def obter_enxadrista_por_id(self, enxadrista_id: str) -> EnxadristaModel | None:
        return self.repository.buscar_por_id(enxadrista_id)

    def criar_enxadrista(self, dados: EnxadristaCreate) -> EnxadristaModel:
        return self.repository.criar(dados)

    def atualizar_enxadrista(self, enxadrista_id: str, dados: EnxadristaUpdate) -> EnxadristaModel | None:
        return self.repository.atualizar(enxadrista_id, dados)

    def deletar_enxadrista(self, enxadrista_id: str) -> bool:
        return self.repository.deletar(enxadrista_id)
