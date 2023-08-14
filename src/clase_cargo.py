from src.clase_ship import Ship

class Cargo(Ship):
    def __init__(self, cargo, quality, draft, crew):
        self.cargo = cargo
        self.quality = quality
        Ship.__init__(self, draft, crew)
        # print("Se creo el Cargo")

    def peso(self):
        peso = self.draft - self.crew * 1.5  # c/tripulacion agrega 1.5 a la diferencia del peso total
        if self.quality == 1:
            peso -= (3.5 + self.cargo)  # se le agrega el peso
        elif self.quality == 0.5:
            peso -= (2 + self.cargo)
        elif self.quality == 0.25:
            peso -= (0.5 + self.cargo)

        if peso < 0:
            raise (f"El barco nro {str(self.cant_ship)} supera su limite de peso")

        return peso

    def is_worth_it(self):
        peso = Cargo.peso(self)
        print(f"Peso botin: {peso}")
        if peso > 20:
            print("¡El cargo tiene un gran botin!")
        else:
            print("El cargo no merece la pena :(")

