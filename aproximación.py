numero = int(input("Elige un numero: "))
epsilon = 0.001
suma = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - numero) >= epsilon and respuesta <= numero:
    print(abs(respuesta**2 - numero))
    respuesta += suma

if abs(respuesta**2 - numero) >= epsilon:
    print(f"No podimos encontrar la respuesta")

else:
    print(f"La raíz cuadrada aproximada de {numero} es {respuesta}")