from algoritmo_genetico.PCG_piva.classes.Pedido import Pedido


class Cromossomo:
    def __init__(self, sequencia_de_producao, nota, entregas):
        self.sequencia_de_producao = sequencia_de_producao
        self.nota = nota
        self.sequencia_de_entrega = entregas

    def __str__(self):
        return (f"Cromossomo(sequencia_de_producao={self.sequencia_de_producao}, "
                f"nota={self.nota}), "
                f"entregas = {self.sequencia_de_entrega}")

    def adicionaEntrega(self, pedido):
        self.sequencia_de_entrega.append(pedido)