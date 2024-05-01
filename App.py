import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    print(dados_json)
else:
    print(f'O erro foi {response.status_code}')

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
