import random
import matplotlib.pyplot as plt
import gera_pedidos
from algoritmo_genetico.PCG_piva.classes.Entrega import Entrega

# Variáveis globais
QUANTIDADE_DE_PEDIDOS = 25
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 3
QUANTIDADE_MAXIMA_DE_ITENS_QUE_UM_MOTOBOY_PODE_LEVAR = QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER * 2 + 10

# Pedidos gerados aleatoriamente
list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)

# Parâmetros do ACO
NUM_FORMIGAS = 20
NUM_ITERACOES = 100
TAXA_EVAPORACAO = 0.5
FEROMONIO_INICIAL = 1.0
ALPHA = 1  # Importância do feromônio
BETA = 2   # Importância da heurística

# Matriz de feromônio
feromonios = [[FEROMONIO_INICIAL for _ in range(QUANTIDADE_DE_PEDIDOS)] for _ in range(QUANTIDADE_DE_PEDIDOS)]

# Função heurística
def heuristica(pedido_atual, pedido_proximo):
    return 1 / (1 + pedido_proximo.quantidade_total_de_itens)

# Encontrar pedido por ID
def encontrar_pedido_por_id(id_procurado):
    for pedido in list_pedidos_gerados:
        if pedido.id == id_procurado:
            return pedido
    return None

# Construir solução para uma formiga
def construir_solucao():
    solucao = []
    pedidos_restantes = list(range(QUANTIDADE_DE_PEDIDOS))
    pedido_atual = random.choice(pedidos_restantes)
    solucao.append(pedido_atual)
    pedidos_restantes.remove(pedido_atual)

    while pedidos_restantes:
        probabilidades = []
        for pedido_proximo in pedidos_restantes:
            pedido_atual_obj = encontrar_pedido_por_id(pedido_atual + 1)
            pedido_proximo_obj = encontrar_pedido_por_id(pedido_proximo + 1)

            feromonio = feromonios[pedido_atual][pedido_proximo]
            heur = heuristica(pedido_atual_obj, pedido_proximo_obj)
            probabilidades.append((feromonio ** ALPHA) * (heur ** BETA))

        soma_probabilidades = sum(probabilidades)
        probabilidades = [p / soma_probabilidades for p in probabilidades]

        pedido_atual = random.choices(pedidos_restantes, weights=probabilidades, k=1)[0]
        solucao.append(pedido_atual)
        pedidos_restantes.remove(pedido_atual)

    return solucao

# Avaliar solução
def avaliar_solucao(solucao):
    nota = 0
    entregas = []

    entrega_atual = Entrega([solucao[0] + 1], 0, encontrar_pedido_por_id(solucao[0] + 1).localidade_para_entrega, 0)
    for id in solucao[1:]:
        pedido_do_loop = encontrar_pedido_por_id(id + 1)
        if pedido_do_loop.localidade_para_entrega.id == entrega_atual.localidade_entrega.id and (entrega_atual.totalDeItems + pedido_do_loop.quantidade_total_de_itens) <= QUANTIDADE_MAXIMA_DE_ITENS_QUE_UM_MOTOBOY_PODE_LEVAR:
            entrega_atual.adicionaEntrega(pedido_do_loop.id)
        else:
            entregas.append(entrega_atual)
            entrega_atual = Entrega([pedido_do_loop.id], pedido_do_loop.quantidade_total_de_itens, pedido_do_loop.localidade_para_entrega, pedido_do_loop.MAIOR_TEMPO_DE_PRODUCAO)

    entregas.append(entrega_atual)
    for entrega in entregas:
        nota += entrega.localidade_entrega.tempo_entrega + entrega.MAIOR_TEMPO_DE_PRODUCAO

    return nota

# Atualização global de feromônios
def atualizar_feromonios(solucoes):
    global feromonios
    for i in range(QUANTIDADE_DE_PEDIDOS):
        for j in range(QUANTIDADE_DE_PEDIDOS):
            feromonios[i][j] *= (1 - TAXA_EVAPORACAO)

    for solucao, nota in solucoes:
        for k in range(len(solucao) - 1):
            i, j = solucao[k], solucao[k + 1]
            feromonios[i][j] += 1 / nota

# Executar ACO
def executar_aco():
    melhores = []
    melhor_solucao_global = None
    menor_nota_global = float('inf')

    for iteracao in range(NUM_ITERACOES):
        solucoes = []
        for _ in range(NUM_FORMIGAS):
            solucao = construir_solucao()
            nota = avaliar_solucao(solucao)
            solucoes.append((solucao, nota))

        # Encontrar a melhor solução da iteração
        melhor_solucao_iteracao = min(solucoes, key=lambda x: x[1])
        melhores.append(melhor_solucao_iteracao[1])

        # Atualizar a melhor solução global
        if melhor_solucao_iteracao[1] < menor_nota_global:
            menor_nota_global = melhor_solucao_iteracao[1]
            melhor_solucao_global = melhor_solucao_iteracao[0]

        atualizar_feromonios(solucoes)



    # Exibir a melhor solução global no terminal
    print("\n>>> MELHOR SOLUÇÃO FINAL <<<")
    print(f"Nota: {menor_nota_global}")
    print("Sequência de Pedidos:")
    for id_pedido in melhor_solucao_global:
        pedido = encontrar_pedido_por_id(id_pedido + 1)
        print(f"  Pedido ID: {pedido.id}, Localidade: {pedido.localidade_para_entrega.id}, Itens: {pedido.quantidade_total_de_itens}")

    # Plotar gráfico
    plt.plot(melhores, label="Melhor solução")
    plt.xlabel("Iteração")
    plt.ylabel("Nota")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    executar_aco()
