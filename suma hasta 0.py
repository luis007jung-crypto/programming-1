# Suma números hasta que ingrese 0

suma = 0
cantidad = 0

print("Ingresa números (0 para salir)")

while True:
    num = float(input("Número: "))
    
    if num == 0:
        break
    
    suma += num      # acumulador
    cantidad += 1    # contador

if cantidad > 0:
    promedio = suma / cantidad
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No ingresaste números")