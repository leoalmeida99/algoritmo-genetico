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
from algoritmo_genetico.PCG_piva.classes.Entrega import Entrega
from algoritmo_genetico.PCG_piva.exemplo_ag.ag1 import nova_pop, imprime_pop, seleciona_pais
from gera_pedidos import gerarPedidos
from classes.Pedido import Pedido

# VARIAVEIS GLOBAIS
QUANTIDADE_DE_PEDIDOS = 10
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 4

TAMANHO_CROMOSSOMO = QUANTIDADE_DE_PEDIDOS
TAMANHO_POPULACAO = TAMANHO_CROMOSSOMO * 1

QUANTIDADE_MAXIMA_DE_ITENS_QUE_UM_MOTOBOY_PODE_LEVAR = QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER * 2 + 1; # 7

# MATRIZ DE POPULAÇÃO
list_populacao = []

list_nova_populacao = []
list_pais = []

# PEDIDOS GERADOS ALEATORIAMENTE
list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)

# A POPULAÇÃO SERÁ UMA MATRIZ COM ID DOS PEDIDOS
def inicializar_populacao():
    print("INICIALIZANDO POPULACAO...")
    for i in range(TAMANHO_POPULACAO):
        gera_sequencia_aleatoria_de_inteiros = random.sample(range(1, QUANTIDADE_DE_PEDIDOS + 1), QUANTIDADE_DE_PEDIDOS)

        cromossomo = Cromossomo(gera_sequencia_aleatoria_de_inteiros, 99999999999999, [])
        list_populacao.append(cromossomo)
    print("POPULACAO CRIADA...")

def imprimir_populacao():
    print("IMPRIMINDO POPULAÇÃO...")
    for cromossomo in list_populacao:
        print(cromossomo)
    print("FIM IMPRESSÃO...")

def imprimir_pedidos_gerados():
    print("IMPRIMINDO PEDIDOS GERADOS")
    for Pedido in list_pedidos_gerados:
        print(Pedido)
    print("FIM IMPRESSÃO DE PEDIDOS GERADOS")

def encontrar_pedido_por_id(id_procurado):
    for pedido in list_pedidos_gerados:
        if pedido.id == id_procurado:
            return pedido
    return None

# if __name__ == '__main__':
#
#     entrega = [10]
#     entrega.append(1)
#
#     print(entrega)
#     # Agrupar os dois primeiros elementos como uma sublista
#     entrega = [entrega]
#     print(entrega)
#     # # Adicionar a segunda sublista
#     entrega2 = [5, 10, 15]
#     entrega.append(entrega2)
#     #
#     print(entrega)
#     # print(entrega[0])

def organizarEntregasCromossomo(cromossomo: Cromossomo):
    # PEGA O PRIMEIRO PEDIDO DO CROMOSSOMO
    primeiro_pedido_cromossomo = encontrar_pedido_por_id(cromossomo.sequencia_de_producao[0])

    entrega_atual = Entrega([primeiro_pedido_cromossomo.id], primeiro_pedido_cromossomo.quantidade_total_de_itens, primeiro_pedido_cromossomo.localidade_para_entrega, primeiro_pedido_cromossomo.MAIOR_TEMPO_DE_PRODUCAO)

    for id in cromossomo.sequencia_de_producao[1:]:
        pedido_do_loop = encontrar_pedido_por_id(id)
        if pedido_do_loop.localidade_para_entrega.id == entrega_atual.localidade_entrega.id and (entrega_atual.totalDeItems + pedido_do_loop.quantidade_total_de_itens) <= QUANTIDADE_MAXIMA_DE_ITENS_QUE_UM_MOTOBOY_PODE_LEVAR:
            entrega_atual.adicionaEntrega(pedido_do_loop.id)
            entrega_atual.totalDeItems += pedido_do_loop.quantidade_total_de_itens

            # VERIFICA SE O MAIOR TEMPO DE PRODUÇÃO DO PEDIDO LOOP, É MAIOR QUE TEMPO DE PRODUÇÃO
            # DA ENTREGA
            if pedido_do_loop.MAIOR_TEMPO_DE_PRODUCAO >= entrega_atual.MAIOR_TEMPO_DE_PRODUCAO:
                entrega_atual.MAIOR_TEMPO_DE_PRODUCAO = pedido_do_loop.MAIOR_TEMPO_DE_PRODUCAO

        else:
            # SALVAR NO CROMOSSOMO A ENTREGA ATUAL

            cromossomo.nota += entrega_atual.localidade_entrega.tempo_entrega + entrega_atual.MAIOR_TEMPO_DE_PRODUCAO
            cromossomo.adicionaEntrega(entrega_atual.pedidos)

            # CRIAR UMA NOVA ENTREGA
            entrega_atual = Entrega([pedido_do_loop.id], pedido_do_loop.quantidade_total_de_itens, pedido_do_loop.localidade_para_entrega, pedido_do_loop.MAIOR_TEMPO_DE_PRODUCAO)

    cromossomo.nota += entrega_atual.localidade_entrega.tempo_entrega + entrega_atual.MAIOR_TEMPO_DE_PRODUCAO
    cromossomo.adicionaEntrega(entrega_atual.pedidos)
    # SALVAR NO CROMOSSOMO A ENTREGA ATUAL


def avaliar_populacao():
    for cromossomo in list_populacao:
        cromossomo.nota = 0
        # FUNÇÃO PARA ORGANIZAR ENTREGAS
        organizarEntregasCromossomo(cromossomo) # ORGANIZA ENTREGA E AVALIA


def imprimir_melhor():
    # Encontra o cromossomo com a menor nota
    melhor_cromossomo = min(list_populacao, key=lambda c: c.nota)

    print(f">>> MELHOR: {melhor_cromossomo}")


def imprimir_pior():
    # Encontra o cromossomo com a maior nota
    pior_cromossomo = max(list_populacao, key=lambda c: c.nota)

    print(f">>> PIOR: {pior_cromossomo}")


def imprimir_medio():
    # Calcula a nota média da população
    if not list_populacao:
        print("População está vazia.")
        return

    nota_media = sum(c.nota for c in list_populacao) / len(list_populacao)

    # Encontra o cromossomo com a nota mais próxima da média
    cromossomo_medio = min(list_populacao, key=lambda c: abs(c.nota - nota_media))

    print(f">>> MÉDIO (Nota média: {nota_media:.2f}): {cromossomo_medio}")


def elitismo(QUANTIDADE_DE_MELHORES_POR_POPULACAO):
    list_populacao.sort(key=lambda c: c.nota)
    for i in range(QUANTIDADE_DE_MELHORES_POR_POPULACAO):
        list_nova_populacao.append(list_populacao[i])


import random

# Função para selecionar pais utilizando roleta
def seleciona_pais():
    list_pais = []
    r_pai1 = random.random()
    r_pai2 = random.random()

    acum = 0
    for i in range(TAMANHO_POPULACAO):
        acum += list_populacao[i].nota  # Nota como aptidão (quanto menor a nota, melhor)
        if acum >= r_pai1:
            list_pais[0] = list_populacao[i]
            break

    acum = 0
    for i in range(TAMANHO_POPULACAO):
        acum += list_populacao[i].nota
        if acum >= r_pai2:
            list_pais[1] = list_populacao[i]
            break


def cruzar(pai1, pai2):
    ponto_corte = random.randint(1, TAMANHO_CROMOSSOMO - 1)  # Ponto de corte para o cruzamento
    filho1_genes = pai1.sequencia_de_producao[:ponto_corte] + pai2.sequencia_de_producao[ponto_corte:]
    filho2_genes = pai2.sequencia_de_producao[:ponto_corte] + pai1.sequencia_de_producao[ponto_corte:]

    # Criar os cromossomos filhos
    filho1 = Cromossomo(filho1_genes, 0, [])
    filho2 = Cromossomo(filho2_genes, 0, [])

    return filho1, filho2

def mutar(cromossomo):
    ponto_mutacao = random.randint(0, TAMANHO_CROMOSSOMO - 1)  # Posição aleatória para mutação
    novo_valor = random.randint(1, QUANTIDADE_DE_PEDIDOS)  # Novo valor para o gene
    cromossomo.sequencia_de_producao[ponto_mutacao] = novo_valor



if __name__ == '__main__':
    inicializar_populacao()
    imprimir_populacao()

    list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)
    imprimir_pedidos_gerados()

    for i in range(10):
        print(f"GERAÇÃO: {i}")
        
        # AVALIAR POP
        avaliar_populacao()

        #IMPRESSÃO
        imprimir_melhor()
        imprimir_pior()
        imprimir_medio()

        # PRESERVAR N MELHORES
        QUANTIDADE_DE_MELHORES_POR_POPULACAO = 5
        elitismo(QUANTIDADE_DE_MELHORES_POR_POPULACAO)

        # GERAR NOVA POPULAÇÃO
        while(QUANTIDADE_DE_MELHORES_POR_POPULACAO < TAMANHO_POPULACAO):
            # SELECIONA PAIS
            seleciona_pais()
            # CRUZA PAIS

            # MUTA FILHOS

            QUANTIDADE_DE_MELHORES_POR_POPULACAO += 2

        list_populacao = list_nova_populacao
        list_nova_populacao = []
