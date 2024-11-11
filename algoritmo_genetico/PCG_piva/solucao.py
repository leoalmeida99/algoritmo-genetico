# ATIVIDADE PRÁTICA DE OTIMIZAÇÃO COMBINATÓRIA UTILIZANDO INTELIGÊNCIA ARTIFICIAL
#
# INTEGRANTES:
# AMANDA NAROAKA
# FELIPE VILJOEN
# LEONARDO DE ALMEIDA PEREIRA
# LUCAS VINICIUS DIMARZIO
# MARCELO BERGER GIL
# VINICIUS LUSTOSA

# IMPORTAÇÕES NECESSÁRIAS PARA A SOLUÇÃO FUNCIONAR
import random
import gera_pedidos
from algoritmo_genetico.PCG_piva.classes.Cromossomo import Cromossomo
from gera_pedidos import gerarPedidos
from classes.Pedido import Pedido

# VARIAVEIS GLOBAIS
QUANTIDADE_DE_PEDIDOS = 15
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 5

TAMANHO_CROMOSSOMO = QUANTIDADE_DE_PEDIDOS
TAMANHO_POPULACAO = TAMANHO_CROMOSSOMO * 10

# MATRIZ DE POPULAÇÃO
list_populacao = []
# PEDIDOS GERADOS ALEATORIAMENTE
list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)
TEMPO_TOTAL_DE_PRODUCAO_PEDIDOS = sum(pedido.tempo_total_de_producao for pedido in list_pedidos_gerados)
TEMPO_TOTAL_DE_ENTREGA_PEDIDOS = sum(pedido.localidade_para_entrega.tempo_entrega for pedido in list_pedidos_gerados)

# A POPULAÇÃO SERÁ UMA MATRIZ COM ID DOS PEDIDOS
def inicializar_populacao():
    print("INICIALIZANDO POPULACAO...")
    for i in range(TAMANHO_POPULACAO):
        gera_sequencia_aleatoria_de_inteiros = random.sample(range(1, QUANTIDADE_DE_PEDIDOS + 1), QUANTIDADE_DE_PEDIDOS)

        cromossomo = Cromossomo(gera_sequencia_aleatoria_de_inteiros, 10, TEMPO_TOTAL_DE_PRODUCAO_PEDIDOS, TEMPO_TOTAL_DE_ENTREGA_PEDIDOS)
        list_populacao.append(cromossomo)

def imprimir_populacao():
    print("IMPRIMINDO POPULAÇÃO...")
    for cromossomo in list_populacao:
        print(cromossomo)

def imprimir_pedidos_gerados():
    print("Pedidos gerados:")
    for Pedido in list_pedidos_gerados:
        print(Pedido)

def avaliar_populacao():
    print('avaliando')
    for cromossomo in list_populacao:
        somador_nota = 0;
        print(cromossomo.sequencia_de_producao)
        for i in range(TAMANHO_CROMOSSOMO):
            # if
            print(cromossomo.sequencia_de_producao[i], end=' ')
        print()
        cromossomo.nota = somador_nota
        # print(cromossomo)


if __name__ == '__main__':

    inicializar_populacao()
    imprimir_populacao()
    

    # list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)
    imprimir_pedidos_gerados()

    print(f"TEMPO TOTAL PARA PRODUZIR TODOS OS PEDIDOS SE FAZER UM POR UM = {TEMPO_TOTAL_DE_PRODUCAO_PEDIDOS}")
    print(f"TEMPO TOTAL DE ENTREGA SE FOR FAZER UM POR UM = {TEMPO_TOTAL_DE_ENTREGA_PEDIDOS}")

    avaliar_populacao()
    imprimir_populacao()