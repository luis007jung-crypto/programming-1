def cifrar_caracter(c, desplazamiento):
    if c.isalpha():
        base = ord('a') if c.islower() else ord('A')
        return chr((ord(c) - base + desplazamiento) % 26 + base)
    return c

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for c in mensaje:
        resultado += cifrar_caracter(c, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

def fuerza_bruta(mensaje):
    for i in range(26):
        print(f"{i}: {descifrar_mensaje(mensaje, i)}")


mensaje = "hola"
cifrado = cifrar_mensaje(mensaje, 3)

print("Cifrado:", cifrado)
print("Descifrado:", descifrar_mensaje(cifrado, 3))

print("\nFuerza bruta:")
fuerza_bruta(cifrado)