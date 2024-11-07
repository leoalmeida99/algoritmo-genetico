from classes.Prato import Prato
from classes.Localidade import Localidade
from classes.Pedido import Pedido


list_localidades = [
    Localidade(1, "Gonzaga", 10),
    Localidade(2, "Aparecida", 15),
    Localidade(3, "Saboó", 20)
]


list_itens = [
    Prato(1, "LANCHE 1", 10),
    Prato(2, "LANCHE 2", 9),
    Prato(3, "LANCHE 3", 13),
    Prato(4, "PIZZA 1", 15),
    Prato(5, "PIZZA 2", 16),
    Prato(6, "PIZZA 3", 14),
    Prato(7, "PORCAO 1", 20),
    Prato(8, "PORCAO 2", 22),
    Prato(9, "PORCAO 3", 25)
]


def exibirLocalidadesEItensDoCardapio():
    print("Localidades:")
    for localidade in list_localidades:
        print(localidade)

    print("\nItens do Cardápio:")
    for Prato in list_itens:
        print(Prato)

def gerarPedidos(quantidade_pedidos: int, quantidade_maxima_de_itens_que_cada_pedido_pode_ter: int):
    return Pedido.gera_Pedidos(quantidade_pedidos, quantidade_maxima_de_itens_que_cada_pedido_pode_ter, list_localidades, list_itens)