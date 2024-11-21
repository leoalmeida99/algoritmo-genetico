from algoritmo_genetico.PCG_piva.classes.Localidade import Localidade

class Entrega:
    def __init__(self, id_pedidos, totalDeItems, localidade_para_entrega: Localidade, MAIOR_TEMPO_DE_PRODUCAO):
        self.pedidos = id_pedidos
        self.totalDeItems = totalDeItems
        self.localidade_entrega = localidade_para_entrega
        self.MAIOR_TEMPO_DE_PRODUCAO = MAIOR_TEMPO_DE_PRODUCAO

    def __str__(self):
        return (f"Itens: {self.pedidos}, Total de Itens: {self.totalDeItems},"
                f"Localidade: {self.localidade_entrega}")

    def adicionaEntrega(self, idPedido):
        self.pedidos.append(idPedido)