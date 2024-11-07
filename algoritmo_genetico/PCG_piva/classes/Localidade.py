class Localidade:
    def __init__(self, id: int, nome: str, tempo_entrega: int):
        self.id = id
        self.nome = nome
        self.tempo_entrega = tempo_entrega

    def __str__(self):
        return f"Localidade(id={self.id}, nome='{self.nome}', tempo_entrega={self.tempo_entrega} minutos)"