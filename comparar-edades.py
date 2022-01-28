def pregunta():

    user1 = input("¿Como te llamas?: ")
    edad1 = int(input(f"¿Qué edad tienes {user1}?: "))
    user2 = input("¿Como se llama tú amigo?: ")
    edad2 = int(input(f"¿Qué edad tiene {user2}?: "))
    
    if edad1 > edad2:
        diferencia = edad1 - edad2
        print(f"{user1} es  {diferencia} años mayor que {user2} ")

    elif edad1 < edad2:
        diferencia = edad2 - edad1
        print(f"{user1} es  {diferencia} años menor que {user2} ")
    else: 
        print(f"{user1} y {user2} tienen la misma edad :D")



pregunta()