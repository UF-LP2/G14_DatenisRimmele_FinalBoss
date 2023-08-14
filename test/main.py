from src.clase_ship import Ship
from src.clase_cruise import Cruise
from src.clase_cargo import Cargo

def main() -> None:
  Maersk = Cargo(15, 1, 10, 30)
  Titanic = Cruise(34,15, 10)
  Algeciras = Cargo(50, 0.5, 100, 15)
  Olimpic = Cruise(15, 62, 5)

  #Maersk.is_worth_it()     #NO
  #Titanic.is_worth_it()    #NO
  #Algeciras.is_worth_it()  #SI
  Olimpic.is_worth_it()    #SI
  try:
    Maersk.peso()
    #Titanic.peso()
    #Algeciras.peso()
    #Olimpic.peso()
  except Exception as e:
    print("Excepcion capturada: " + str(e))

if __name__ == "__main__":
  main()
