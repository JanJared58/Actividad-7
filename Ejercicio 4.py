alumnos = []

def agregar_alumno(nombre, edad, calificaciones):
    alumno = (nombre, edad, calificaciones) 
    alumnos.append(alumno)  
    print(f"Alumno '{nombre}' agregado exitosamente.")

def mostrar_alumnos():
    if alumnos:
        print("\nLista de alumnos:")
        for i, alumno in enumerate(alumnos, 1):
            nombre, edad, calificaciones = alumno
            print(f"{i}. Nombre: {nombre}, Edad: {edad}, Calificaciones: {calificaciones}")
    else:
        print("\nNo hay alumnos registrados aún.")

# Interacción con el usuario
print("Sistema de Registro de Alumnos")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar un alumno")
    print("2. Mostrar la lista de alumnos")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        try:
            edad = int(input(f"Ingresa la edad de {nombre}: "))
            calificaciones = list(map(float, input(f"Ingrese las calificaciones de {nombre}, separadas por comas: ").split(",")))
            agregar_alumno(nombre, edad, calificaciones)
        except ValueError:
            print("Por favor, ingresa datos válidos para la edad y/o calificaciones.")
    elif opcion == "2":
        mostrar_alumnos()
    elif opcion == "3":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
