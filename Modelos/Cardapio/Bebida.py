from Modelos.Cardapio.Item_cardapio import Itemcardapio
class Bebida(Itemcardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho