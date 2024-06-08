


from models.botella import Botella


class Botella_Controller:
    def __init__(self) -> None:
        self.botellas = []

    def create_botella(self, capacidad: float, color: str, dimensiones: dict) -> None:
        botella = Botella(capacidad=capacidad, color=color, dimensiones=dimensiones)
        self.botellas.append(botella)
        
    def pop_botella(self) -> Botella:
        botella = self.botellas[-1]
        self.botellas.pop()
        return botella

    def get_botellas(self) -> list:
        return self.botellas