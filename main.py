import csv
from src.clase_ship import Ship
from src.clase_cargo import Cargo
from src.clase_cruise import Cruise


def verifico(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def main() -> None:
    ship = []
    with open("caca.csv", newline='') as csvfile:
        lector = csv.reader(csvfile, delimiter=',', quotechar='|')
        # next(csvfile, None)
        for row in lector:
            if(verifico(row[0]) and verifico(row[1])) is True:
                if row[3] == '':
                    if row[2] == '':
                        aux = Ship(row[0], row[1])
                        ship.append(aux)
                    elif verifico(row[2]) is True:
                        aux = Cruise(row[2], row[0], row[1])
                        ship.append(aux)
                else:
                    if row[2] == '':
                        if verifico(row[3]) is True:
                            aux = Cargo(0, row[3], row[0], row[1])
                            ship.append(aux)
                    else:
                        if(verifico(row[2]) and verifico(row[3])) is True:
                            aux = Cargo(row[2], row[3], row[0], row[1])
                            ship.append(aux)

        for i in range(len(ship)):
            # print(str(ship[i]))
            valor = ship[i].is_worth_it()


if __name__ == "__main__":
    main()
