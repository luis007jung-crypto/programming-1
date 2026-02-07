import math

print("Calculadora básica")

while True:
    print("\nSelecciona una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")

    opcion = input("Ingresa el número de la opción: ")

    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Error: opción no válida")
        continue

    try:
        if opcion == "6":
            num = float(input("Ingresa el número: "))
            if num < 0:
                print("Error: no se puede calcular la raíz de un número negativo")
            else:
                print("Resultado:", math.sqrt(num))
            continue

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            print("Resultado:", num1 + num2)
        elif opcion == "2":
            print("Resultado:", num1 - num2)
        elif opcion == "3":
            print("Resultado:", num1 * num2)
        elif opcion == "4":
            if num2 == 0:
                print("Error: no se puede dividir entre cero")
            else:
                print("Resultado:", num1 / num2)
        elif opcion == "5":
            print("Resultado:", num1 ** num2)

    except ValueError:
        print("Error: debes ingresar números válidos")

