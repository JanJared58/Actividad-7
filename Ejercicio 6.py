temperaturas = []

def calcular_promedio(temperaturas):
    total_temperatura = sum(temp for _, temp in temperaturas)
    return total_temperatura / len(temperaturas)

print("Registro de temperaturas semanales")

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for dia in dias_semana:
    try:
        temperatura = float(input(f"Ingrese la temperatura para {dia}: "))
        temperaturas.append((dia, temperatura))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la temperatura.")

print("\nTemperaturas registradas:")
for dia, temp in temperaturas:
    print(f"{dia}: {temp}°C")

if temperaturas:
    promedio = calcular_promedio(temperaturas)
    print(f"\nLa temperatura promedio de la semana es: {promedio:.2f}°C")
else:
    print("\nNo se ingresaron datos válidos.")
