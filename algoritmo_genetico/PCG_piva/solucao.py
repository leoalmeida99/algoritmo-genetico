# ATIVIDADE PRÁTICA DE OTIMIZAÇÃO COMBINATÓRIA UTILIZANDO INTELIGÊNCIA ARTIFICIAL
#
# INTEGRANTES:
# AMANDA NAROAKA
# FELIPE VILJOEN
# LEONARDO DE ALMEIDA PEREIRA
# LUCAS VINICIUS DIMARZIO
# MARCELO BERGER GIL

# IMPORTAÇÕES NECESSÁRIAS PARA A SOLUÇÃO FUNCIONAR
import random
import gera_pedidos
from gera_pedidos import gerarPedidos
from classes.Pedido import Pedido

# VARIAVEIS GLOBAIS
QUANTIDADE_DE_PEDIDOS = 15
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 5


TAMANHO_CROMOSSOMO = QUANTIDADE_DE_PEDIDOS
TAMANHO_POPULACAO = TAMANHO_CROMOSSOMO * 10

#MATRIZ DE POPULAÇÃO
populacao = []


def inicializar_populacao():
    print("INICIALIZANDO POPULACAO...")
    for i in range(TAMANHO_POPULACAO):
        # Gera uma linha com X números inteiros, e esses inteiros não seja repetido.
        linha = random.sample(range(1, QUANTIDADE_DE_PEDIDOS + 1), QUANTIDADE_DE_PEDIDOS)
        populacao.append(linha)

def imprimir_populacao():
    print("IMPRIMINDO POPULAÇÃO")
    quantidade_de_linhas = TAMANHO_POPULACAO
    quantidade_de_colunas = QUANTIDADE_DE_PEDIDOS
    for i in range(quantidade_de_linhas):
        for j in range(quantidade_de_colunas):
            print(populacao[i][j], end='')
            print(" ", end='')
        print("")
    print("FIM DA IMPRESSÃO")


if __name__ == '__main__':

    inicializar_populacao()
    imprimir_populacao()

    # PEDIDOS GERADOS ALEATORIAMENTE
    list_pedidos = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)

    print("Pedidos gerados:")
    for Pedido in list_pedidos:
        print(Pedido)
