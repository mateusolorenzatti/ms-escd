import urllib.request
import urllib.error
import json

BASE_URL = "http://localhost:8001/contatos/"

def get(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

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
    pretty_print("Listando contatos existentes (GET /contatos/):", get(BASE_URL))

    novo_contato = {
        "id": 300,
        "nome": "Teste REST",
        "telefones": [{"numero": "5499999999", "tipo": "movel"}, {"numero": "5432000001", "tipo": "fixo"}],
        "categoria": "pessoal"
    }

    pretty_print("Criando novo contato (POST /contatos/):", post(BASE_URL, novo_contato))

    pretty_print("Listando contatos atualizados:", get(BASE_URL))

    pretty_print("Buscando contato pelo ID (GET /contatos/300):", get(BASE_URL + "300"))
