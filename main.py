from src.clase_ship import Ship


def main() -> None:
  print("Hello World")
  barco1 = Ship(40, 20)
  try:
    barco1.calcular_peso()
  except Exception as e:
    print("Excepcion capturada: " + str(e))

if __name__ == "__main__":
  main()
