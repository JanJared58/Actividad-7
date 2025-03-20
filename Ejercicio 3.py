diccionario = {}

def agregar_traduccion(palabra, traduccion):
    diccionario[palabra] = traduccion
    print(f"La palabra '{palabra}' ha sido agregada con la traducción '{traduccion}'.")

def buscar_traduccion(palabra):
    if palabra in diccionario:
        return f"La traducción de '{palabra}' es '{diccionario[palabra]}'."
    else:
        return "Palabra no encontrada."

print("Bienvenido al diccionario de traducciones.")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar una palabra y su traducción")
    print("2. Buscar la traducción de una palabra")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        palabra = input("Ingresa la palabra en el idioma original: ").lower()
        traduccion = input(f"Ingresa la traducción de '{palabra}': ").lower()
        agregar_traduccion(palabra, traduccion)
    elif opcion == "2":
        palabra = input("Ingresa la palabra que deseas buscar: ").lower()
        print(buscar_traduccion(palabra))
    elif opcion == "3":
        print("¡Gracias por usar el diccionario de traducciones! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
