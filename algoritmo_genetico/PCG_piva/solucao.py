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
QUANTIDADE_DE_PEDIDOS = 3
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 3

TAMANHO_CROMOSSOMO = QUANTIDADE_DE_PEDIDOS
TAMANHO_POPULACAO = TAMANHO_CROMOSSOMO * 1

# MATRIZ DE POPULAÇÃO
list_populacao = []
# PEDIDOS GERADOS ALEATORIAMENTE
list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)

# A POPULAÇÃO SERÁ UMA MATRIZ COM ID DOS PEDIDOS
def inicializar_populacao():
    print("INICIALIZANDO POPULACAO...")
    for i in range(TAMANHO_POPULACAO):
        gera_sequencia_aleatoria_de_inteiros = random.sample(range(1, QUANTIDADE_DE_PEDIDOS + 1), QUANTIDADE_DE_PEDIDOS)

        cromossomo = Cromossomo(gera_sequencia_aleatoria_de_inteiros, 10)
        list_populacao.append(cromossomo)

def imprimir_populacao():
    print("IMPRIMINDO POPULAÇÃO...")
    for cromossomo in list_populacao:
        print(cromossomo)

def imprimir_pedidos_gerados():
    print("Pedidos gerados:")
    for Pedido in list_pedidos_gerados:
        print(Pedido)

def encontrar_pedido_por_id(id_procurado):
    for pedido in list_pedidos_gerados:
        if pedido.id == id_procurado:
            return pedido
    return None

def avaliar_populacao():
    print('avaliando')

    for cromossomo in list_populacao:
        somador_nota = 0;
        for id in cromossomo.sequencia_de_producao:
            pedido = encontrar_pedido_por_id(id)
            print(pedido.id)
            for item in pedido.lista_itens_pedido:
                print(item)
            print(pedido.localidade_para_entrega)



if __name__ == '__main__':
    inicializar_populacao()
    # imprimir_populacao()

    list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)
    # imprimir_pedidos_gerados()

    avaliar_populacao()
    # imprimir_populacao()