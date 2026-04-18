# 1. Crear tupla con coordenadas de Escuintla
coordenadas = (14.3050, -90.7850)

# 2. Función que desempaqueta y retorna lat y lon
def obtener_coordenadas(tupla):
    lat, lon = tupla
    return lat, lon  # ← usamos return

latitud, longitud = obtener_coordenadas(coordenadas)
print("Latitud:", latitud)
print("Longitud:", longitud)


# 3. Función que retorna (min, max, promedio)
def estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return minimo, maximo, promedio  # ← return de 3 valores

numeros = [5, 15, 25, 35, 45]
minimo, maximo, promedio = estadisticas(numeros)

print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Promedio:", promedio)


# 4. Función que crea y retorna un diccionario
def crear_distancias():
    return {
        ("Escuintla", "Guate"): 58,
        ("Escuintla", "Antigua"): 45
    }

distancias = crear_distancias()

for ruta, km in distancias.items():
    print(ruta, ":", km, "km")


# 5. Intentar modificar tupla (error)
# coordenadas[0] = 15.0  # ❌ Las tuplas no se pueden modificar