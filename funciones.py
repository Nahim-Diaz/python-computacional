def enumeración(objetivo):
    contador = 0
    while contador**2 < objetivo:
        print(contador)
        contador += 1
    
    if contador**2 == objetivo:
        print(f"La raíz cuadrada de {objetivo} es {contador}")
    else:
        print(f"{objetivo} no tiene raíz cuadrada exacta")


def aproximación(objetivo, epsilon):
    suma = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo))
        respuesta += suma
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"No podimos encontrar la respuesta")
    else:
        print(f"La raíz cuadrada aproximada de {objetivo} es {respuesta}")


def busqueda(objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')



menu = """Bienvenido, este programa sirve para calcular la raíz cuadrada de un numero usando distintos tipos de algoritmos.

Algoritmos:  
    a)Enumeración exahustiva (raices exactas) 
    b)Aproximación (No es exacta)
    c)Busqueda Binaria (más eficiente)

Selecciona un algoritmo (escribe el literal): """

opción = input(menu)
objetivo = int(input("Escribe el numero del cual quieras averiguar su raíz cuadrada: "))


if opción == "a":
    enumeración(objetivo)

elif opción == "b":
    epsilon = float(input("Escribe el valor de epsilon (Mientras más pequeño será más preciso y lento) ejemplo 0.01: "))
    aproximación(objetivo, epsilon)


elif opción == "c":
    epsilon = float(input("Escribe el valor de epsilon (Mientras más pequeño será más preciso y lento) ejemplo 0.01: "))
    busqueda(objetivo, epsilon)

else:
    print("elige una opción validad :D")



