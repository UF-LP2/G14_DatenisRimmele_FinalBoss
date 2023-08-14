from src.clase_ship import Ship


class Cruise(Ship):
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers
        Ship.__init__(self, draft, crew)
        # print("Se creo el Crucero")

    def peso(self):
        peso = self.draft - self.passengers * 2.25 - self.crew * 1.5  # diferencia de paso
        if peso < 0:
            raise (f"El barco nro {str(self.cant_ship)} supera su limite de peso")
        return peso

    def is_worth_it(self):
        peso = Cruise.peso(self)
        print(f"Peso botin: {peso}")
        if peso > 20:
            print("¡El crucero tiene un gran botin!")
        else:
            print("El crucero no merece la pena :(")

