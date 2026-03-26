# 1. Crear diccionario con información personal
persona = {
    "nombre": "Luis",
    "edad": 21,
    "ciudad": "Masagua",
    "lenguaje_favorito": "Español"
}

# 2. Agregar nueva clave 'universidad'
persona["universidad"] = "Universidad san pablo de Guatemala"

# 3. Modificar el valor de 'edad'
persona["edad"] = 21

# 4. Iterar con .items() e imprimir cada par
print("Datos de la persona:")
for clave, valor in persona.items():
    print(clave, ":", valor)

# 5. Verificar si 'email' existe
if "email" in persona: 
    print("El email existe")
else:
    print("El email NO existe")

# 6. Usar .get() para acceder a 'telefono' sin error
telefono = persona.get("telefono", "54614832")
print("Teléfono:", telefono)