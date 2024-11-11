class Cromossomo:
    def __init__(self, sequencia_de_producao, nota, tempo_producao, tempo_de_entrega):
        self.sequencia_de_producao = sequencia_de_producao
        self.nota = nota
        self.tempo_producao = tempo_producao
        self.tempo_entrega = tempo_de_entrega

    def __str__(self):
        return (f"Cromossomo(sequencia_de_producao={self.sequencia_de_producao}, "
                f"nota={self.nota}), "
                f"tempo produção = {self.tempo_producao}, "
                f"tempo entrega = {self.tempo_entrega}")