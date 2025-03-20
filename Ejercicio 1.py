productos = {
    "manzana": 10,
    "plátano": 5,
    "naranja": 8,
    "pera": 12,
    "uva": 15
}

def buscar_precio(producto):
    if producto in productos:
        return f"El precio de {producto} es ${productos[producto]}."
    else:
        return "Producto no encontrado."

print("Bienvenido al sistema de consulta de precios.")
while True:
    producto = input("Ingrese el nombre del producto (o escriba 'salir' para finalizar): ").lower()
    if producto == "salir":
        print("¡Gracias por usar el sistema! Hasta luego.")
        break
    print(buscar_precio(producto))
