def saludo(nombre):
    saludo = f"Hola, {nombre} es un gusto conocerte"
    print(f"{saludo} sabias que ese mensaje tiene {len(saludo)} carácteres")


nombre = input("¿Como te llamas?: ")
saludo(nombre)
