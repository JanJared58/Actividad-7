import math

def distancia_al_origen(punto):
    x, y = punto
    return math.sqrt(x**2 + y**2)

def ordenar_por_distancia(puntos):
    return sorted(puntos, key=distancia_al_origen)

puntos = [(3, 4), (1, 1), (0, 0), (5, 12), (-3, -4)]
puntos_ordenados = ordenar_por_distancia(puntos)
print("Puntos ordenados según su distancia al origen:")
print(puntos_ordenados)
