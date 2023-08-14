from src.clase_ship import Ship

class Cargo(Ship):
    def __init__(self, draft, crew, cargo, quality):
        self.cargo = cargo
        self.quality = quality
        Ship.__init__(self, draft, crew)
        print("Se creo el Cargo")

    def is_worth_it(self):
        peso = self.crew * 1.5
        if self.quality == 1:
            peso += 3.5
        elif self.quality == 0.5:
            peso += 2
        elif self.quality == 0.25:
            peso += 0.5