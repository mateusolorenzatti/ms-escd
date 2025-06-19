import enum
import strawberry
from typing import List

# Criar novos Enums baseados nos valores dos modelos
class GQLTipoTelefoneEnum(enum.Enum):
    fixo = "fixo"
    movel = "movel"
    comercial = "comercial"

class GQLCategoriaContatoEnum(enum.Enum):
    pessoal = "pessoal"
    familiar = "familiar"
    comercial = "comercial"

# Decorar com strawberry.enum
GQLTipoTelefone = strawberry.enum(GQLTipoTelefoneEnum)
GQLCategoriaContato = strawberry.enum(GQLCategoriaContatoEnum)

@strawberry.type
class GQLTelefone:
    numero: str
    tipo: GQLTipoTelefone

@strawberry.type
class GQLContato:
    id: int
    nome: str
    telefones: List[GQLTelefone]
    categoria: GQLCategoriaContato
