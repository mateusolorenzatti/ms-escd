from typing import List
from app.core.models import Contato, CategoriaContato, Telefone, TipoTelefone

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
