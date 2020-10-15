# Con esto usamos creamos una funcion
def conversacion(mensaje):
    print(".")
    print(".")
    print(".")
    print(mensaje)
    print(".")
    print(".")
    print(".")

opciones = int(input("Elige una opción (1 - 2 - 3): "))
if opciones == 1:
    conversacion("Elegiste la opción 1")
elif opciones == 2:
    conversacion("Elegiste la opción 2")
elif opciones == 3:
    conversacion("Elegiste la opción 3")
else:
    conversacion("Escribe una opcion correcta")