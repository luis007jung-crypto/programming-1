historial = []
def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)

def calcular_total(subtotal, propina):
    return subtotal + propina

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: número de personas inválido"
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    return subtotal * (1 - descuento_pct / 100)

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Calcular propina")
    print("2. Dividir cuenta")
    print("3. Descuento + propina")
    print("4. Salir")
    print("5. Ver historial")  # bonus

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige opción: ")

        try:
            if opcion == "1":
                subtotal = float(input("Subtotal: "))
                porcentaje = float(input("Propina (%): "))
                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)
                print("Total:", total)
                historial.append(f"Propina: {total}")

            elif opcion == "2":
                total = float(input("Total: "))
                personas = int(input("Personas: "))
                resultado = dividir_cuenta(total, personas)
                print("Cada uno paga:", resultado)
                historial.append(f"División: {resultado}")

            elif opcion == "3":
                subtotal = float(input("Subtotal: "))
                descuento = float(input("Descuento (%): "))
                nuevo = aplicar_descuento(subtotal, descuento)
                porcentaje = float(input("Propina (%): "))
                propina = calcular_propina(nuevo, porcentaje)
                total = calcular_total(nuevo, propina)
                print("Total final:", total)
                historial.append(f"Descuento+Propina: {total}")

            elif opcion == "4":
                print("Saliendo...")
                break

            elif opcion == "5":
                print("\nHistorial:")
                for h in historial:
                    print(h)

            else:
                print("Opción inválida")

        except:
            print("Error: entrada inválida")
main()