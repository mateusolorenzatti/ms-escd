from fastapi import APIRouter, HTTPException
from typing import List

from app.core.models import Contato
from app.core.db import db

router = APIRouter(
    prefix="/contatos",
    tags=["Contatos"]
)

@router.post("/", response_model=Contato)
def criar_contato(contato: Contato):
    db.append(contato)
    return contato

@router.get("/{contato_id}", response_model=Contato)
def obter_contato(contato_id: int):
    for contato in db:
        if contato.id == contato_id:
            return contato
    raise HTTPException(status_code=404, detail="Contato não encontrado")

@router.get("/", response_model=List[Contato])
def listar_contatos():
    return db
