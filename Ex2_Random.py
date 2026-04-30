import random
numero = random.randint(1, 100)
intentos = 0
print(f"Adivina el número secreto (1-100). Tienes 5 intentos.")

while intentos < 5:
    intentos += 1
    eleccion = int(input(f"Adivina el número: "))
    print(f"Intento {intentos}/5")
    if eleccion == numero:
        print(f"¡Acertaste!")
        break
    elif eleccion < numero:
        print(f"El número secreto es MAYOR que {eleccion}")
    else:
        print(f"El número secreto es MENOR que {eleccion}")
if eleccion != numero:
    print(f"Se acabaron los intentos, el número secreto era {numero}. Fin del juego")