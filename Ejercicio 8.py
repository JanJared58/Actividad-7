estudiantes = []

def agregar_estudiante(nombre, asignaturas, amigos):
    estudiante = {
        "nombre": nombre,
        "asignaturas": asignaturas,
        "amigos": amigos
    }
    estudiantes.append(estudiante)
    print(f"Estudiante '{nombre}' agregado exitosamente.")

def mostrar_estudiantes():
    if estudiantes:
        print("\nLista de estudiantes:")
        for i, estudiante in enumerate(estudiantes, 1):
            print(f"{i}. Nombre: {estudiante['nombre']}")
            print(f"   Asignaturas y calificaciones: {estudiante['asignaturas']}")
            print(f"   Amigos: {estudiante['amigos']}")
    else:
        print("\nNo hay estudiantes registrados aún.")

print("Sistema de Registro de Estudiantes")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar un estudiante")
    print("2. Mostrar la lista de estudiantes")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del estudiante: ")
        asignaturas = {}
        print("Ingresa las asignaturas y calificaciones (escribe 'listo' para terminar):")
        while True:
            asignatura = input("Asignatura: ")
            if asignatura.lower() == "listo":
                break
            try:
                calificacion = float(input(f"Calificación en {asignatura}: "))
                asignaturas[asignatura] = calificacion
            except ValueError:
                print("Por favor, ingresa una calificación válida.")
        
        amigos = input("Ingresa los nombres de los amigos separados por comas: ").split(",")
        amigos = [amigo.strip() for amigo in amigos]  
        agregar_estudiante(nombre, asignaturas, amigos)
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
