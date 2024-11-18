class Cromossomo:
    def __init__(self, sequencia_de_producao, nota):
        self.sequencia_de_producao = sequencia_de_producao
        self.nota = nota

    def __str__(self):
        return (f"Cromossomo(sequencia_de_producao={self.sequencia_de_producao}, "
                f"nota={self.nota})")