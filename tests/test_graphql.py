import urllib.request
import json

GQL_URL = "http://localhost:8001/graphql"
REST_URL = "http://localhost:8001/contatos/"

def post(url, data):
    data_bytes = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, method="POST", headers={
        "Content-Type": "application/json"
    })
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

def pretty_print(title, data):
    print(f"\n >> {title}")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print('-'*50)

if __name__ == "__main__":
    query_list = {
        "query": """
        query {
          contatos {
            id
            nome
            categoria
            telefones {
              numero
              tipo
            }
          }
        }
        """
    }
    pretty_print("Listando contatos via GraphQL (query):",
                 post(GQL_URL, query_list)["data"]["contatos"])

    novo_contato = {
        "id": 400,
        "nome": "GraphQL Teste",
        "telefones": [{"numero": "5121210001", "tipo": "fixo"}],
        "categoria": "comercial"
    }
    pretty_print("Criando contato via REST (POST /contatos/):",
                 post(REST_URL, novo_contato))

    pretty_print("Re-listando contatos via GraphQL:",
                 post(GQL_URL, query_list)["data"]["contatos"])

    query_by_id = {
        "query": """
        query {
          contato(id: 400) {
            id
            nome
            categoria
            telefones {
              numero
              tipo
            }
          }
        }
        """
    }
    pretty_print("Buscando contato por ID via GraphQL:",
                 post(GQL_URL, query_by_id)["data"]["contato"])
