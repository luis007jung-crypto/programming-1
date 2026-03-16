nombre = input("nombre del estudiante: ")
grado = input("grado que cursa: ")

nota1 = float(input("primer bimestre: "))
nota2 = float(input("segundo bimestre: "))
nota3 = float(input("tercer bimestre: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 61:
    estado = "APRUEBA"
else:
    estado = "REPRUEBA"

print("\n--- RESULTADOS ---")
print(f"Estudiante: {nombre}")
print(f"Grado: {grado}")
print(f"Promedio: {promedio}")
print(f"Estado: {estado}")