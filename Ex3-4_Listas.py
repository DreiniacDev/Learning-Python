notas = [85, 42, 91, 55, 78, 38, 95]

# Forma larga (con for)
aprobados = []
for n in notas:
    if n >= 60:
        aprobados.append(n)
print(aprobados)   


# Forma corta (list comprehension)
aprobados = [n for n in notas if n >= 60]
print(aprobados)  # → [85, 91, 78, 95]


# También puedes transformar valores
dobles = [n * 2 for n in notas]
print(dobles)     # → [170, 84, 182, 110, 156, 76, 190]