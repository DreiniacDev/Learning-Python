notas = [85, 42, 91, 55, 78, 38, 95, 60, 73, 29]

aprobados = [n for n in notas if n >= 60]
reprobados = [n for n in notas if n < 60]
while True:
    print("1. Resultados")
    print("2. Estadisticas")
    print("3. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        print(f"Aprobados ({len(aprobados)}): {aprobados}")
        print(f"Reprobados ({len(reprobados)}): {reprobados}")
    elif opcion == "2":
        promedio = (sum(notas)/len(notas))
        mas_alta = max(notas)
        mas_baja = min(notas)
        print(f"Promedio general: {promedio}")
        print(f"Nota más baja: {mas_baja}")
        print(f"Nota más alta: {mas_alta}")
    elif opcion == "3":
        break