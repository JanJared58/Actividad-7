ventas = []

def agregar_venta(producto, mes, cantidad_vendida):
    venta = {
        "producto": producto,
        "mes": mes,
        "cantidad_vendida": cantidad_vendida
    }
    ventas.append(venta)
    print(f"Venta agregada: Producto: {producto}, Mes: {mes}, Cantidad Vendida: {cantidad_vendida}")

def mostrar_ventas():
    if ventas:
        print("\nVentas registradas:")
        for i, venta in enumerate(ventas, 1):
            print(f"{i}. Producto: {venta['producto']}, Mes: {venta['mes']}, Cantidad Vendida: {venta['cantidad_vendida']}")
    else:
        print("\nNo hay ventas registradas aún.")

print("Sistema de Registro de Ventas")

while True:
    print("\n¿Qué quieres hacer?")
    print("1. Agregar una venta")
    print("2. Mostrar las ventas registradas")
    print("3. Salir")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        mes = input("Ingresa el mes de la venta: ")
        try:
            cantidad_vendida = int(input(f"Ingrese la cantidad vendida de {producto}: "))
            agregar_venta(producto, mes, cantidad_vendida)
        except ValueError:
            print("Por favor, ingresa un valor numérico válido para la cantidad vendida.")
    elif opcion == "2":
        mostrar_ventas()
    elif opcion == "3":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")
