nombre = input("Cuál es tu nombre? ")
edad = int(input("Cuántos años tienes? "))
ciudad = input("En qué ciudad vives? ")

print("=" * 30)

print(f"Hola soy {nombre.upper()}")

print("=" * 30)

print(f"Edad: {edad} años")
print(f"Ciudad: {ciudad}")
print(f"Para 100 años: faltan {100 - edad} años")

print("=" * 30)