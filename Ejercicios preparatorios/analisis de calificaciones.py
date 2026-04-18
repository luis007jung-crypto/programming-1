def promedio(notas):
    return sum(notas) / len(notas)


def mayor(notas):
    m = notas[0]
    for n in notas:
        if n > m:
            m = n
    return m


def menor(notas):
    m = notas[0]
    for n in notas:
        if n < m:
            m = n
    return m


def contar_aprobados(notas, minimo=61):
    contador = 0
    for n in notas:
        if n >= minimo:
            contador += 1
    return contador


def histograma(notas):  # Bonus
    for n in notas:
        print(f"{n}: {'*' * (n // 5)}")  # escala simple


def reporte(notas):
    print("📊 REPORTE DE NOTAS")
    print("-------------------")
    print(f"Promedio: {promedio(notas):.2f}")
    print(f"Mayor: {mayor(notas)}")
    print(f"Menor: {menor(notas)}")
    print(f"Aprobados: {contar_aprobados(notas)} / {len(notas)}")
    print("\nHistograma:")
    histograma(notas)


# Prueba
if __name__ == "__main__":
    notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
    reporte(notas)