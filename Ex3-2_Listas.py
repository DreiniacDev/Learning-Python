contacto = {
    "nombre": "Carlos",
    "tel":    "555-1234",
    "ciudad": "Monterrey"
}

# Solo claves
for clave in contacto:
    print(clave)

# Clave y valor juntos
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")