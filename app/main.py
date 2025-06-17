from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from app.models import Contato, CategoriaContato, Telefone, TipoTelefone

app = FastAPI()

db: List[Contato] = [
        Contato(
            id=1,
            nome="João Silva",
            telefones=[
                Telefone(numero="11987654321", tipo=TipoTelefone.movel),
                Telefone(numero="1134567890", tipo=TipoTelefone.fixo)
            ],
            categoria=CategoriaContato.familiar
        ),
        Contato(
            id=2,
            nome="Empresa XYZ",
            telefones=[
                Telefone(numero="1140004000", tipo=TipoTelefone.comercial)
            ],
            categoria=CategoriaContato.comercial
        ),
        Contato(
            id=3,
            nome="Ana Paula",
            telefones=[
                Telefone(numero="11999998888", tipo=TipoTelefone.movel)
            ],
            categoria=CategoriaContato.pessoal
        )
]

@app.post("/contatos/", response_model=Contato)
def criar_contato(contato: Contato):
    db.append(contato)
    return contato

@app.get("/contatos/{contato_id}", response_model=Contato)
def obter_contato(contato_id: int):
    for contato in db:
        if contato.id == contato_id:
            return contato
    raise HTTPException(status_code=404, detail="Contato não encontrado")

@app.get("/contatos/", response_model=List[Contato])
def listar_contatos():
    return db