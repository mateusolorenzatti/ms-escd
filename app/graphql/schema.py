import strawberry
from typing import List, Optional

from app.core.db import db 
from app.graphql.types import GQLContato

@strawberry.type
class Query:
    @strawberry.field
    def contato(self, id: int) -> Optional[GQLContato]:
        for contato in db:
            if contato.id == id:
                return contato
        return None

    @strawberry.field
    def contatos(self) -> List[GQLContato]:
        return db

schema = strawberry.Schema(query=Query)
