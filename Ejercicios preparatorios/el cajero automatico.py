def calcular_billetes(monto):
    if monto % 20 != 0:
        print("❌ Error: el monto debe ser múltiplo de 20")
        return None

    billetes = [200, 100, 50, 20]
    resultado = {}

    for b in billetes:
        cantidad = monto // b
        if cantidad > 0:
            resultado[b] = cantidad
            monto %= b

    salida = ", ".join([f"{v}x Q{k}" for k, v in resultado.items()])
    print(salida)

    return resultado


if __name__ == "__main__":
    calcular_billetes(370)