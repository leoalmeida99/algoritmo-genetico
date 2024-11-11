from algoritmo_genetico.PCG_piva.enum.ETipoPrato import ETipoPrato
from classes.Prato import Prato
from classes.Localidade import Localidade
from classes.Pedido import Pedido


list_localidades = [
    Localidade(1, "Gonzaga", 10),
    Localidade(2, "Aparecida", 15),
    Localidade(3, "Saboó", 20)
]


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

def exibirLocalidadesEItensDoCardapio():
    print("Localidades:")
    for localidade in list_localidades:
        print(localidade)

    print("\nItens do Cardápio:")
    for Prato in list_itens:
        print(Prato)

def gerarPedidos(quantidade_pedidos: int, quantidade_maxima_de_itens_que_cada_pedido_pode_ter: int):
    return Pedido.gera_Pedidos(quantidade_pedidos, quantidade_maxima_de_itens_que_cada_pedido_pode_ter, list_localidades, list_itens)