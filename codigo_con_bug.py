edad = input("Ingresa tu edad: ")

# Prints de debug para investigar
print(f"DEBUG tipo: {type(edad)}")
print(f"DEBUG valor: [{edad}]")
print(f"DEBUG len: {len(edad)}")

if edad >= 18:   # BUG: edad es string, 18 es int
    print("Acceso permitido")
else:
    print("Acceso denegado")