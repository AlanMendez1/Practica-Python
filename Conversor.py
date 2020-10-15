menu = """
Bienvenido al conversor de monedas!!!

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuántos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    NAME = input("Escriba su nombre: ")
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(NAME + ", " + "tienes $" + dolares + " USD")


opcion = int(input(menu))

if opcion == 1:
    conversor("COP", 3700)
elif opcion == 2:
    conversor("ARS", 77)
elif opcion == 3:
    conversor("MXN", 21)
else:
    print("¡Ingresa una opción correcta!")