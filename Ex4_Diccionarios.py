#Agendda de contactos

#Una agenda donde puedes agregar y listar contactos. El polograma tiene un menú que se repite hasta que eliges salir.

agenda = {}

while True:
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Listar contactos")
    print("4. Modificar contacto")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        agenda [nombre] = telefono
        print("Contacto guardado")
    elif opcion == "2":
        nombre = input("Buscar: ")
        if nombre in agenda:
            print(f"{nombre}: {agenda[nombre]}")
        else:
            print(f"{nombre} no está en tu agenda.")
    elif opcion == "3":
        print("--- Tus contactos ---")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    elif opcion == "4":
        nombre = input("Buscar: ")
        if nombre in agenda:
            telefono_actual = agenda[nombre]
            print(f"{nombre}: {agenda[nombre]}")
            while True:
                print("1. Modificar nombre")
                print("2. Modificar teléfono")
                print("3. Modificar ambos")
                print("4. Salir")
                opcion = input("Elige una opción: ")
                if opcion == "1":
                    nuevo_nombre = input("Nuevo nombre: ")
                    del agenda[nombre]
                    agenda[nuevo_nombre] = telefono_actual
                elif opcion == "2":
                    agenda [nombre] = input("Nuevo teléfono: ")
                elif opcion == "3":
                    del agenda[nombre]
                    nuevo_nombre = input("Nuevo nombre: ")
                    nuevo_tel = input("Nuevo teléfono: ")
                    agenda[nuevo_nombre] = nuevo_tel
                elif opcion == "4":
                    break
        else:
            print(f"{nombre} no está en tu agenda.")
    elif opcion == "5":
        break