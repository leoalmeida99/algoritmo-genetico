from enum import Enum

class ETipoPrato(Enum):
    LANCHE = 1
    PIZZA = 2
    PORCAO = 3

# # Acessando valores do enum
# print(ETipoPrato.LANCHE)         # Saída: DiaSemana.SEGUNDA
# print(ETipoPrato.LANCHE.name)    # Saída: SEGUNDA
# print(ETipoPrato.LANCHE.value)   # Saída: 1
#
# # Iterando sobre os valores do enum
# for dia in ETipoPrato:
#     print(dia)