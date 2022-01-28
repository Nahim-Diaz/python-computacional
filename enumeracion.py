objetivo = int(input("Escoge un entero: "))

contador = 0

while contador**2 < objetivo:
    print(contador)
    contador += 1

if contador**2 == objetivo:
    print(f"La raíz cuadrada de {objetivo} es {contador}")

else:
    print(f"{objetivo} no tiene raíz cuadrada exacta")