# app/core/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "Torneio de Xadrez API"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"

    # Configuração do banco SQLite
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASE_URL: str = f"sqlite:///{os.path.join(BASE_DIR, '..', 'chess.db')}"

    # Segurança
    SECRET_KEY: str = "chave-super-secreta"  # depois podemos colocar no .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"  # variáveis podem ser sobrescritas por este arquivo

@lru_cache
def get_settings() -> Settings:
    return Settings()
