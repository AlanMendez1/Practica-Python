menu = """
Bienvenido al conversor de monedas!!! 🌍

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:

    COP = input("Inserte COP ")
    NAME = input("Escriba su nombre: ")
    COP = float(COP)
    USDprecio = 3700
    USD = COP / USDprecio
    USD = round(USD,2)
    USD = str(USD)
    print(NAME + ", " + "tienes $" + USD + " USD")
elif opcion == 2:
    ARS = input("Inserte ARS ")
    NAME = input("Escriba su nombre: ")
    ARS = float(ARS)
    USDprecio = 77
    USD = ARS / USDprecio
    USD = round(USD,2)
    USD = str(USD)
    print(NAME + ", " + "tienes $" + USD + " USD")

elif opcion == 3:
    MXN = input("Inserte MXN ")
    NAME = input("Escriba su nombre: ")
    MXN = float(MXN)
    USDprecio = 21
    USD = MXN / USDprecio
    USD = round(USD,2)
    USD = str(USD)
    print(NAME + ", " + "tienes $" + USD + " USD")
else:
    print("¡Ingresa una opción correcta!")