import random

numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

while intentos < max_intentos:
    intento = int(input("Adivina (1-100): "))
    intentos += 1

    if intento < numero_secreto:
        print("📈 Más alto")
    elif intento > numero_secreto:
        print("📉 Más bajo")
    else:
        print(f"🎉 ¡Correcto en {intentos} intentos!")
        break
else:
    print(f"❌ Perdiste. El número era {numero_secreto}")