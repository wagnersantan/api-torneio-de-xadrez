import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError  # Correção aqui

# A URL de conexão pode ser passada como variável de ambiente para segurança
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

try:
    # Tenta criar a conexão com o MongoDB
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)  # 5 segundos de timeout para tentar conectar
    # Verifica se a conexão foi bem-sucedida
    client.admin.command('ping')
    print("Conexão com o MongoDB realizada com sucesso!")
    
    # Conecta ao banco de dados e à coleção
    db = client["torneio_xadrez"]
    torneio_collection = db["torneios"]
except ServerSelectionTimeoutError as e:  # Alteração aqui
    print(f"Erro ao conectar ao MongoDB: {e}")
    db = None  # Caso haja erro, db será None e a aplicação pode tratar isso
    torneio_collection = None
