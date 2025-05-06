# app/repositories/torneio_repository.py

import datetime
from bson import ObjectId
from app.models.torneio_model import Torneio
from app.database.connection import db

def cadastrar_torneio(torneio: Torneio):
    collection = db["torneios"]
    torneio_dict = torneio.dict()

    data_inicio = torneio_dict.get("data_inicio")
    data_fim = torneio_dict.get("data_fim")

    if isinstance(data_inicio, datetime.date) and not isinstance(data_inicio, datetime.datetime):
        torneio_dict["data_inicio"] = datetime.datetime.combine(data_inicio, datetime.datetime.min.time())

    if isinstance(data_fim, datetime.date) and not isinstance(data_fim, datetime.datetime):
        torneio_dict["data_fim"] = datetime.datetime.combine(data_fim, datetime.datetime.min.time())

    collection.insert_one(torneio_dict)
    return torneio_dict

def listar_torneios():
    collection = db["torneios"]
    torneios = list(collection.find())
    for t in torneios:
        t["_id"] = str(t["_id"])
    return torneios
