import sys
import os
import pytest_asyncio  # Importando pytest_asyncio

# Adiciona o diretório raiz do projeto (onde está o arquivo `app/`) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient
from app.servidor import app  # Corrigido para refletir a estrutura do projeto

# Usando pytest_asyncio.fixture para criar a fixture assíncrona
@pytest_asyncio.fixture
async def async_client():
    # Aqui, removemos o parâmetro `app` e passamos apenas a `base_url`
    async with AsyncClient(base_url="http://test") as client:
        yield client


