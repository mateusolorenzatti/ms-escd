from enum import Enum
from typing import List
from pydantic import BaseModel

class TipoTelefone(str, Enum):
    movel = "movel"
    fixo = "fixo"
    comercial = "comercial"

class CategoriaContato(str, Enum):
    familiar = "familiar"
    pessoal = "pessoal"
    comercial = "comercial"

class Telefone(BaseModel):
    numero: str
    tipo: TipoTelefone

class Contato(BaseModel):
    id: int
    nome: str
    telefones: List[Telefone]
    categoria: CategoriaContato