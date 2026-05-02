class Estudiante:
    def _init_(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def aprobado(self):
        return self.promedio() >= 61


# Uso rápido
e = Estudiante("Luis", "123", "Ingeniería")
e.agregar_nota(70)
e.agregar_nota(80)

print("Promedio:", e.promedio())
print("¿Aprobado?:", e.aprobado())