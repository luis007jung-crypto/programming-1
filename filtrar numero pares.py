# Filtrar números pares de una lista

numeros = [12, 7, 23, 8, 42, 15, 36, 9]

# ✅ Método 1: Bucle tradicional
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print("Método 1:", pares)  # [12, 8, 42, 36]


# ✅ Método 2: List comprehension (más pythonico)
pares = [n for n in numeros if n % 2 == 0]

print("Método 2:", pares)  # [12, 8, 42, 36]


# ✅ Método 3: filter() + lambda
pares = list(filter(lambda n: n % 2 == 0, numeros))

print("Método 3:", pares)  # [12, 8, 42, 36]