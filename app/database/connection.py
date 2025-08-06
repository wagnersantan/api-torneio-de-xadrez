from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./chess.db"

# Criar engine SQLite
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Criar sessão para conexão com o banco
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Classe base para os modelos
Base = declarative_base()

# Função para dependência no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
