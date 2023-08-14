class Ship(object):
    cont_bar = 0

    def __init__(self, draft, crew):
        self.crew = crew
        self.draft = draft
        Ship.cont_bar = Ship.cont_bar + 1
        print("Se creo el barco, nro" + str(self.cont_bar))
        
    def calcular_peso(self):
        peso = self.draft - self.crew * 1.5
        if peso <= 0:
            raise "El barco supera se limite de peso"
        else:
            return peso

    def is_worth_it(self):
        try:
            valor = Ship.calcular_peso(self)
            if 0 < valor <= 20:
                print('El barco no merece ser saqueado')
            else:
                print('El barco merece ser saqueado')
        except Exception as e:
            print("Excepcion capturada:" + str(e))
