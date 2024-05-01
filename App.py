import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            'item': item['Item'],
            'price': item['price'],
            'description': item['description']
        })
else:
    print(f'O erro foi {response.status_code}')
print(dados_restaurante['McDonald’s'])
# from Modelos.restaurante import Restaurante
# from Modelos.Cardapio.bebida import Bebida
# from Modelos.Cardapio.prato import Prato
#
# restaurante_praca = Restaurante('praça', 'Gourmet')
# bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
# prato_paozinho = Prato('Paozinho',2.00,'O melhor pão da cidade')
# restaurante_praca.adicionar_no_cardapio(bebida_suco)
# restaurante_praca.adicionar_no_cardapio(prato_paozinho)
# bebida_suco.aplicar_desconto()
# prato_paozinho.aplicar_desconto()
# def main():
#     restaurante_praca.exibir_cardapio()
#
#
# if __name__ == '__main__':
#     main()
