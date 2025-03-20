estudiantes = {}

def agregar_estudiante(nombre, calificaciones):
    estudiantes[nombre] = calificaciones
    print(f"Estudiante '{nombre}' agregado con calificaciones: {calificaciones}")

def mostrar_calificaciones(nombre):
    if nombre in estudiantes:
        return f"Las calificaciones de {nombre} son: {estudiantes[nombre]}"
    else:
        return "Estudiante no encontrado."

print("Sistema de Registro de Calificaciones de Estudiantes")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar estudiante")
    print("2. Mostrar calificaciones de un estudiante")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del estudiante: ")
        try:
            calificaciones = list(map(float, input(f"Ingrese las calificaciones de {nombre}, separadas por comas: ").split(",")))
            agregar_estudiante(nombre, calificaciones)
        except ValueError:
            print("Iingresa calificaciones válidas.")
    elif opcion == "2":
        nombre = input("Ingresa el nombre del estudiante cuyas calificaciones deseas ver: ")
        print(mostrar_calificaciones(nombre))
    elif opcion == "3":
        print("Adios.")
        break
    else:
        print("Opción no válida, selecciona 1, 2 o 3.")
