"""
Módulo de funções utilitárias da API.
Aqui colocamos funções auxiliares que podem ser usadas em qualquer parte do projeto.
"""

from datetime import datetime
import uuid


def gerar_id():
    """
    Gera um identificador único (UUID4) como string.
    Útil para criar IDs de enxadristas, torneios, partidas, etc.
    """
    return str(uuid.uuid4())


def data_hora_atual():
    """
    Retorna a data e hora atuais no formato ISO 8601.
    """
    return datetime.utcnow().isoformat()


def validar_campo_obrigatorio(valor, nome_campo):
    """
    Verifica se um campo obrigatório foi preenchido.
    Se não for preenchido, levanta uma exceção ValueError.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"O campo '{nome_campo}' é obrigatório.")
    return True
