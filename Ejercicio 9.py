agenda = []

def agregar_contacto(nombre, telefono, correos):
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "correos": correos
    }
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")

def buscar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            return f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Correos: {', '.join(contacto['correos'])}"
    return "Contacto no encontrado."

def eliminar_contacto(nombre):
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            agenda.remove(contacto)
            print(f"Contacto '{nombre}' eliminado exitosamente.")
            return
    print("Contacto no encontrado.")

print("Bienvenido a la Agenda de Contactos")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = input("Selecciona una opción (1/2/3/4): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
        correos = input(f"Ingrese los correos electrónicos de {nombre}, separados por comas: ").split(",")
        correos = [correo.strip() for correo in correos] 
        agregar_contacto(nombre, telefono, correos)
    elif opcion == "2":
        nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
        print(buscar_contacto(nombre))
    elif opcion == "3":
        nombre = input("Ingresa el nombre del contacto que deseas eliminar: ")
        eliminar_contacto(nombre)
    elif opcion == "4":
        print("¡Gracias por usar la Agenda de Contactos! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
