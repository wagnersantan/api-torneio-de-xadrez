from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import get_db
from app.services.torneio_service import TorneioService
from app.schemas.torneio_schema import TorneioCreate, TorneioRead

router = APIRouter(prefix="/torneios", tags=["torneios"])

@router.get("/", response_model=List[TorneioRead], summary="Listar todos os torneios")
def listar_torneios(db: Session = Depends(get_db)):
    service = TorneioService(db)
    return service.listar_torneios()

@router.post("/", response_model=TorneioRead, status_code=status.HTTP_201_CREATED, summary="Criar novo torneio")
def criar_torneio(torneio: TorneioCreate, db: Session = Depends(get_db)):
    service = TorneioService(db)
    try:
        return service.criar_torneio(torneio)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
