def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15


def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()

    # Paso 1: convertir TODO a Celsius
    if origen == "C":
        c = valor
    elif origen == "F":
        c = fahrenheit_a_celsius(valor)
    elif origen == "K":
        c = valor - 273.15
    elif origen == "R":  # Bonus Rankine
        c = (valor - 491.67) * 5/9
    else:
        return None

    # Paso 2: de Celsius al destino
    if destino == "C":
        return c
    elif destino == "F":
        return celsius_a_fahrenheit(c)
    elif destino == "K":
        return celsius_a_kelvin(c)
    elif destino == "R":  # Bonus Rankine
        return celsius_a_fahrenheit(c) + 459.67
    else:
        return None


# Ejemplos
if __name__ == "__main__":
    print(convertir(5, "C", "F"))  # 77.0
    print(convertir(77, "F", "C"))  # 25.0
    print(convertir(0, "C", "K"))   # 273.15
    print(convertir(32, "F", "K"))  # 273.15
    print(convertir(300, "K", "F")) # 80.33 aprox
    print(convertir(100, "C", "R")) # Bonus