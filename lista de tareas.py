# Lista de tareas (CLI)

tareas = []

while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append(tarea)
        print("✅ Agregada")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas")
        else:
            for i, t in enumerate(tareas, 1):
                print(f"{i}. {t}")

    elif opcion == "3":
        if not tareas:
            print("No hay tareas para eliminar")
        else:
            try:
                idx = int(input("# a eliminar: "))
                if 1 <= idx <= len(tareas):
                    eliminada = tareas.pop(idx - 1)
                    print(f"🗑️ Eliminada: {eliminada}")
                else:
                    print("Número inválido")
            except ValueError:
                print("Entrada inválida")

    elif opcion == "4":
        print("👋 Saliendo...")
        break

    else:
        print("Opción no válida")