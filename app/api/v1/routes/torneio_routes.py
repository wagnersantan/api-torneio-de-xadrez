from fastapi import APIRouter, HTTPException
from app.schemas.torneio_schema import TorneioCreate, TorneioResponse
from app.services.torneio_service import criar_torneio, listar_torneios
from typing import List

router = APIRouter(prefix="/torneios", tags=["Torneios"])

@router.post("/", response_model=TorneioResponse)
async def criar_torneio_route(torneio: Torneio):
    try:
        return await criar_torneio(torneio)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[TorneioResponse])
async def listar_torneios_route():
    try:
        return await listar_torneios()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

