from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# Rest
from app.rest.controllers import router

# GraphQL
from app.graphql.schema import schema

graphql_app = GraphQLRouter(schema)

app = FastAPI()

app.include_router(router)
app.include_router(graphql_app, prefix="/graphql")
