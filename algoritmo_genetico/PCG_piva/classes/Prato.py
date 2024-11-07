class Prato:
    def __init__(self, id: int, nome: str, tempo_producao: int):
        self.id = id
        self.nome = nome
        self.tempo_producao = tempo_producao

    def __str__(self):
        return f"Prato(id={self.id}, nome='{self.nome}', tempo_producao={self.tempo_producao} minutos)"