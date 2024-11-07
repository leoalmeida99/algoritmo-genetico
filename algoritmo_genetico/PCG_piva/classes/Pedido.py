from classes.Prato import Prato
from classes.Localidade import Localidade
import random

class Pedido:
    def __init__(self, id: int, localidade_para_entrega: Localidade, lista_itens: list[Prato]):
        self.id = id
        self.localidade_para_entrega = localidade_para_entrega
        self.lista_itens_pedido = lista_itens

    def __str__(self):
        itens = ', '.join([item.nome for item in self.lista_itens_pedido])
        return (f"Pedido(id={self.id}, "
                f"localidade_para_entrega={self.localidade_para_entrega.nome}, "
                f"itens_pedido=[{itens}])")

    @staticmethod
    def gera_Pedidos(quantidade_pedidos: int, quantidade_maxima_de_itens_que_cada_pedido_pode_ter: int,
                     list_localidades: list[Localidade], list_itens: list[Prato]):

        pedidos = []

        for i in range(1, quantidade_pedidos + 1):
            # Escolhe uma localidade para o pedido de forma aleatória
            localidade = random.choice(list_localidades)

            # Escolhe um número entre 1 e X, X sendo a quantidade maxima de itens para cada pedido
            quantidade_itens = random.randint(1, quantidade_maxima_de_itens_que_cada_pedido_pode_ter)

            # Gera uma lista de itens aleatória (de 1 a X itens), podendo repetir itens
            itens_pedido = random.choices(list_itens, k=quantidade_itens)

            # Cria uma instância de Pedido e adiciona à lista
            pedido = Pedido(i, localidade, itens_pedido)
            pedidos.append(pedido)

        return pedidos