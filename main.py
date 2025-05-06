
from fastapi import FastAPI
from app.routes.enxadrista_routes import router as enxadrista_routes
from app.routes.torneio_routes import router as torneio_routes
from app.database.connection import db, torneio_collection  # Certifique-se de que isso está importado corretamente
from datetime import datetime

app = FastAPI()

# Inserir um torneio de teste, garantindo que o banco de dados e a coleção sejam criados
def inserir_torneio_teste():
    torneio_data = {
        "nome": "Torneio Teste",
        "data": "2025-05-01",
        "local": "Local Teste",
        "jogadores": ["Jogador 1", "Jogador 2"]
    }

    # Verificar se o torneio já existe
    if db["torneios"].count_documents({"nome": torneio_data["nome"]}) == 0:
        torneio_collection.insert_one(torneio_data)
        print("Torneio de teste inserido!")
    else:
        print("Torneio de teste já existe.")

# Rota raiz de boas-vindas
@app.get("/")
def read_root():
    inserir_torneio_teste()  # Inserindo o torneio de teste apenas se não existir
    return {"message": "API do Torneio de Xadrez funcionando!"}

# Registrando as rotas
print("Registrando as rotas...")  # Verificação
app.include_router(enxadrista_routes, prefix="/enxadrista", tags=["Enxadristas"])
app.include_router(torneio_routes, prefix="/torneios", tags=["Torneios"])

print("Rotas registradas!")  # Verificação
