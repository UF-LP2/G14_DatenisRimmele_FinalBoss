from src.clase_ship import Ship

class Cruise(Ship):
    def __init__(self, draft, crew, passengers):
        self.passengers = passengers
        Ship.__init__(self, draft, crew)
        print("Se creo el Crusero")

    def is_worth_it(self):
        peso = 0
        peso = self.passengers*2.25 + self.crew*1.5
        worthit = self.draft - peso
        return worthit