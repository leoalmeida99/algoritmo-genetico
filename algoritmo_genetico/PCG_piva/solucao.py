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
import matplotlib.pyplot as plt

import gera_pedidos
from algoritmo_genetico.PCG_piva.classes.Cromossomo import Cromossomo
from algoritmo_genetico.PCG_piva.classes.Entrega import Entrega

# VARIAVEIS GLOBAIS
QUANTIDADE_DE_PEDIDOS = 15
QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER = 3

TAMANHO_CROMOSSOMO = QUANTIDADE_DE_PEDIDOS
TAMANHO_POPULACAO = TAMANHO_CROMOSSOMO * 2

QUANTIDADE_MAXIMA_DE_ITENS_QUE_UM_MOTOBOY_PODE_LEVAR = QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER * 2 + 1;

list_populacao = []

list_nova_populacao = []
list_pais = []

list_filhos = []

melhor_cromossomo = []
melhores_nota = []
piores_nota = []
medios_nota = []

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

def organizarEntregasCromossomo(cromossomo: Cromossomo):
    # PEGA O PRIMEIRO PEDIDO DO CROMOSSOMO
    primeiro_pedido_cromossomo = encontrar_pedido_por_id(cromossomo.sequencia_de_producao[0])

    cromossomo.sequencia_de_entrega.clear()

    entrega_atual = Entrega([primeiro_pedido_cromossomo.id], primeiro_pedido_cromossomo.quantidade_total_de_itens, primeiro_pedido_cromossomo.localidade_para_entrega, primeiro_pedido_cromossomo.MAIOR_TEMPO_DE_PRODUCAO)

    indice_entrega = 1  # Índice da entrega atual, começa em 1 para a primeira entrega

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
            penalidade = calcular_penalidade_localidade(entrega_atual.localidade_entrega.tempo_entrega, indice_entrega)
            cromossomo.nota += entrega_atual.localidade_entrega.tempo_entrega + entrega_atual.MAIOR_TEMPO_DE_PRODUCAO + penalidade
            cromossomo.adicionaEntrega(entrega_atual.pedidos)

            # CRIAR UMA NOVA ENTREGA
            entrega_atual = Entrega([pedido_do_loop.id], pedido_do_loop.quantidade_total_de_itens, pedido_do_loop.localidade_para_entrega, pedido_do_loop.MAIOR_TEMPO_DE_PRODUCAO)

            indice_entrega += 1  # Incrementa o índice da entrega

    # Aplica penalidade para a última entrega
    penalidade = calcular_penalidade_localidade(entrega_atual.localidade_entrega.tempo_entrega, indice_entrega)
    cromossomo.nota += entrega_atual.localidade_entrega.tempo_entrega + entrega_atual.MAIOR_TEMPO_DE_PRODUCAO + penalidade
    # SALVAR NO CROMOSSOMO A ENTREGA ATUAL
    cromossomo.adicionaEntrega(entrega_atual.pedidos)


def calcular_penalidade_localidade(tempo_entrega_localidade, indice_entrega):
    """
    Calcula a penalidade para uma entrega com base no tempo de entrega da localidade e no índice da entrega.
    """
    fator_punicao = 2  # Ajuste este valor para aumentar ou diminuir o impacto da punição
    return fator_punicao * tempo_entrega_localidade * (1 / indice_entrega)

def avaliar_populacao():
    for cromossomo in list_populacao:
        cromossomo.nota = 0
        # FUNÇÃO PARA ORGANIZAR ENTREGAS
        organizarEntregasCromossomo(cromossomo) # ORGANIZA ENTREGA E AVALIA


def imprimir_melhor():
    melhor_cromossomo = min(list_populacao, key=lambda c: c.nota)
    melhores_nota.append(melhor_cromossomo.nota)

    print(f">>> MELHOR: {melhor_cromossomo}")


def imprimir_pior():
    pior_cromossomo = max(list_populacao, key=lambda c: c.nota)
    piores_nota.append(pior_cromossomo.nota)

    print(f">>> PIOR: {pior_cromossomo}")


def imprimir_medio():
    # Calcula a nota média da população
    nota_media = sum(c.nota for c in list_populacao) / len(list_populacao)

    # Encontra o cromossomo com a nota mais próxima da média
    cromossomo_medio = min(list_populacao, key=lambda c: abs(c.nota - nota_media))

    medios_nota.append(cromossomo_medio.nota)

    print(f">>> MÉDIO (Nota média: {nota_media:.2f}): {cromossomo_medio}")


def elitismo(QUANTIDADE_DE_MELHORES_POR_POPULACAO):
    list_populacao.sort(key=lambda c: c.nota)
    for i in range(QUANTIDADE_DE_MELHORES_POR_POPULACAO):
        list_nova_populacao.append(list_populacao[i])

# Função para selecionar pais utilizando roleta viciada
def seleciona_pais():
    # Lista de pais selecionados
    list_pais.clear()

    # Calcular soma das notas (fitness inverso, pois menor é melhor)
    soma_fitness = sum(1 / cromossomo.nota for cromossomo in list_populacao)

    # Criar uma roleta cumulativa baseada em fitness inverso
    roleta = []
    acumulador = 0
    for cromossomo in list_populacao:
        probabilidade = (1 / cromossomo.nota) / soma_fitness
        acumulador += probabilidade
        roleta.append(acumulador)

    # Selecionar dois pais
    for _ in range(2):
        r = random.random()  # Número aleatório entre 0 e 1
        for i, limite in enumerate(roleta):
            if r <= limite:
                list_pais.append(list_populacao[i])
                break

def cruzar():
    # Garantir que temos dois pais na lista
    if len(list_pais) < 2:
        print("Erro: não há pais suficientes para cruzar!")

    pai1, pai2 = list_pais[0], list_pais[1]

    # Ponto de corte para cruzamento
    ponto_corte = random.randint(1, TAMANHO_CROMOSSOMO - 1)

    # Geração inicial de filhos
    filho1_genes = pai1.sequencia_de_producao[:ponto_corte]
    filho2_genes = pai2.sequencia_de_producao[:ponto_corte]

    # Preenchendo o restante dos genes dos pais, garantindo IDs únicos
    filho1_genes += [gene for gene in pai2.sequencia_de_producao if gene not in filho1_genes]
    filho2_genes += [gene for gene in pai1.sequencia_de_producao if gene not in filho2_genes]

    # Criar os cromossomos filhos
    filho1 = Cromossomo(filho1_genes, 0, [])
    filho2 = Cromossomo(filho2_genes, 0, [])

    # Adicionar filhos à nova população
    list_nova_populacao.append(filho1)
    list_nova_populacao.append(filho2)

def exibir_melhor_producao_e_entrega_cromossomo(cromossomo):
    print("\n--- Melhor Cromossomo ---")
    print(f"Nota final: {cromossomo.nota}")
    print(f"Quantidade de entregas: {len(cromossomo.sequencia_de_entrega)}")
    print("Detalhes das entregas:")

    for i, entrega in enumerate(cromossomo.sequencia_de_entrega, start=1):
        quantidade_itens = sum(encontrar_pedido_por_id(pedido_id).quantidade_total_de_itens for pedido_id in entrega)
        localidade = encontrar_pedido_por_id(entrega[0]).localidade_para_entrega
        print(f"Entrega {i}:")
        print(f"  Localidade de entrega: {localidade.nome}")
        print(f"  IDs dos pedidos: {', '.join(map(str, entrega))}")
        print(f"  Quantidade total de itens: {quantidade_itens}")
    print("--- Fim do Cromossomo ---\n")


if __name__ == '__main__':
    inicializar_populacao()
    imprimir_populacao()

    list_pedidos_gerados = gera_pedidos.gerarPedidos(QUANTIDADE_DE_PEDIDOS, QUANTIDADE_MAXIMA_DE_ITENS_QUE_CADA_PEDIDO_PODE_TER)
    imprimir_pedidos_gerados()

    for i in range(100):
        print(f"GERAÇÃO: {i}")
        
        # AVALIAR POP
        avaliar_populacao()

        #IMPRESSÃO
        imprimir_melhor()
        imprimir_pior()
        imprimir_medio()

        # PRESERVAR N MELHORES
        QUANTIDADE_DE_MELHORES_POR_POPULACAO = 4
        elitismo(QUANTIDADE_DE_MELHORES_POR_POPULACAO)

        # GERAR NOVA POPULAÇÃO
        while(QUANTIDADE_DE_MELHORES_POR_POPULACAO < TAMANHO_POPULACAO):
            # SELECIONA PAIS
            seleciona_pais()
            # CRUZA PAIS
            cruzar()

            QUANTIDADE_DE_MELHORES_POR_POPULACAO += 2

        list_populacao = list_nova_populacao
        list_nova_populacao = []

    exibir_melhor_producao_e_entrega_cromossomo(list_populacao[0])

    # Plotar gráfico de convergência
    plt.figure(figsize=(10, 6))
    plt.plot(melhores_nota, label='Melhor')
    plt.plot(piores_nota, label='Pior')
    plt.plot(medios_nota, label='Média', linestyle='--')

    plt.title('Gráfico de Convergência')
    plt.xlabel('Geração')
    plt.ylabel('Nota')
    plt.legend()
    plt.grid(True)
    plt.show()