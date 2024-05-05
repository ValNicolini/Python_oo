
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    '''
    Endpoint q exibe a mensagem 'Hello: World
    '''
    return {'Hello: World'}

@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str=(Query(default=None))):
    '''
     Endpoint para visualizar o cardápio dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
            })
        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}
    else:
        return {f'Erro: {response.status_code} - {response.text}'}

# uvicorn main:app --reload <- rodar no terminal