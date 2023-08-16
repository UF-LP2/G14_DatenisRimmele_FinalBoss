class Ship(object):
    cant_ship = 0

    def __init__(self, draft, crew):
        self.draft = float(draft)
        self.crew = float(crew)
        Ship.cant_ship = Ship.cant_ship + 1
        self.identificaion = Ship.cant_ship
        print("Se creo el barco, nro " + str(self.cant_ship))

    def peso(self):
        peso = self.draft - self.crew * 1.5
        if peso <= 0:
            raise Exception(f"El barco {str(self.identificaion)} supera su limite de peso")
        return peso

    def is_worth_it(self):
        try:
            peso = self.peso()
            if peso < 20:
                print(f"El crucero no merece la pena :(")
            else:
                print("¡El crucero tiene un gran botin!")
        except Exception as e:
            print(str(e))