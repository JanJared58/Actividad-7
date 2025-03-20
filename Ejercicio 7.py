compras = []

def agregar_compra(producto, cantidad, precio_unitario):
    compras.append((producto, cantidad, precio_unitario))
    print(f"Compra agregada: Producto: {producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario}")

def calcular_total(compras):
    total = sum(cantidad * precio_unitario for _, cantidad, precio_unitario in compras)
    return total

print("Registro de compras de la tienda")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar una compra")
    print("2. Mostrar el total gastado")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        try:
            cantidad = int(input(f"Ingrese la cantidad de '{producto}': "))
            precio_unitario = float(input(f"Ingrese el precio unitario de '{producto}': "))
            agregar_compra(producto, cantidad, precio_unitario)
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos para la cantidad y el precio.")
    elif opcion == "2":
        total = calcular_total(compras)
        print(f"\nEl total gastado por el cliente es: ${total:.2f}")
    elif opcion == "3":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
