from typing import List
from app.core.models import Contato, CategoriaContato, Telefone, TipoTelefone

db: List[Contato] = [
    Contato(
        id=1,
        nome="Alice",
        telefones=[
            Telefone(numero="51987654321", tipo=TipoTelefone.movel),
            Telefone(numero="5134567890", tipo=TipoTelefone.fixo)
        ],
        categoria=CategoriaContato.familiar
    ),
    Contato(
        id=2,
        nome="Blablatech Corp.",
        telefones=[
            Telefone(numero="112312312", tipo=TipoTelefone.comercial)
        ],
        categoria=CategoriaContato.comercial
    ),
    Contato(
        id=3,
        nome="Carl",
        telefones=[
            Telefone(numero="2199009900", tipo=TipoTelefone.movel)
        ],
        categoria=CategoriaContato.pessoal
    )
]
