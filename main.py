from fastapi import FastAPI
from app.api.v1.routes.enxadrista_routes import router as enxadrista_routes
from app.api.v1.routes.torneio_routes import router as torneio_routes



# Comentado o import da conexão com Mongo para evitar erro
# from app.database.connection import db, torneio_collection  
from datetime import datetime

app = FastAPI()

# Comentei a função para não tentar acessar o banco
# def inserir_torneio_teste():
#     torneio_data = {
#         "nome": "Torneio Teste",
#         "data": "2025-05-01",
#         "local": "Local Teste",
#         "jogadores": ["Jogador 1", "Jogador 2"]
#     }
#     if db["torneios"].count_documents({"nome": torneio_data["nome"]}) == 0:
#         torneio_collection.insert_one(torneio_data)
#         print("Torneio de teste inserido!")
#     else:
#         print("Torneio de teste já existe.")

@app.get("/")
def read_root():
    # inserir_torneio_teste()  # Desativado por enquanto
    return {"message": "API do Torneio de Xadrez funcionando sem banco (modo simulado)"}

print("Registrando as rotas...")  
app.include_router(enxadrista_routes, prefix="/enxadrista", tags=["Enxadristas"])
app.include_router(torneio_routes, prefix="/torneios", tags=["Torneios"])

print("Rotas registradas!")
