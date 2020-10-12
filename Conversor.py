COP = input("Inserte COP ")
NAME = input("Su nombre, por favor ")
COP = float(COP)
USDprecio = 3700
USD = COP / USDprecio
USD = round(USD,2)
USD = str(USD)
print(NAME + ", " + "tienes $" + USD + " USD")
