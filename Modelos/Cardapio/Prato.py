from Modelos.Cardapio.Item_cardapio import Itemcardapio
class Prato(Itemcardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao