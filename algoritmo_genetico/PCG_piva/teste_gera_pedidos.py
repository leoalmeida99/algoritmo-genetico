# VARIAVEIS GLOBAIS
from algoritmo_genetico.PCG_piva import gera_pedidos
from algoritmo_genetico.PCG_piva.classes.Prato import Prato
from algoritmo_genetico.PCG_piva.enum.ETipoPrato import ETipoPrato




pedidos_gerados = []

QUANTIDADE_DE_PEDIDOS = 15
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 5

def imprimir_pedidos_gerados():
    print("Pedidos gerados:")
    for Pedido in pedidos_gerados:
        print(Pedido)

list_itens = [
    Prato(1, "X-Salada", 9, ETipoPrato.LANCHE),
    Prato(2, "X-Bacon", 10, ETipoPrato.LANCHE),
    Prato(3, "X-Tudo", 13, ETipoPrato.LANCHE),
    Prato(4, "Mussarela", 15, ETipoPrato.PIZZA),
    Prato(5, "Paulista", 16, ETipoPrato.PIZZA),
    Prato(6, "Portuguesa", 14, ETipoPrato.PIZZA),
    Prato(7, "Frango a passarinho", 20, ETipoPrato.PORCAO),
    Prato(8, "Fritas", 22, ETipoPrato.PORCAO),
    Prato(9, "Fritas com bacon", 25, ETipoPrato.PORCAO)
]

if __name__ == '__main__':
    pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS,
                                                QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)

    imprimir_pedidos_gerados()

    for prato in list_itens:
        print(prato)