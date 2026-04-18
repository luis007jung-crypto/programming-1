def validar_password(password):
    especiales = "!@#$%"

    tiene_mayuscula = False
    tiene_digito = False
    tiene_especial = False
    no_tres_iguales = True

    for i in range(len(password)):
        c = password[i]

        if c.isupper():
            tiene_mayuscula = True
        if c.isdigit():
            tiene_digito = True
        if c in especiales:
            tiene_especial = True

        # Bonus: 3 iguales seguidos
        if i < len(password) - 2:
            if password[i] == password[i+1] == password[i+2]:
                no_tres_iguales = False

    if (
        len(password) >= 8 and
        tiene_mayuscula and
        tiene_digito and
        tiene_especial and
        no_tres_iguales
    ):
        return True
    else:
        return False


def diagnosticar_password(password):
    especiales = "!@#$%"

    if len(password) < 8:
        print("❌ Mínimo 8 caracteres")
    if not any(c.isupper() for c in password):
        print("❌ Falta mayúscula")
    if not any(c.isdigit() for c in password):
        print("❌ Falta número")
    if not any(c in especiales for c in password):
        print("❌ Falta carácter especial")

    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            print("❌ Tiene 3 caracteres iguales seguidos")
            break


# Uso
if __name__ == "__main__":
    pwd = input("Contraseña: ")

    if validar_password(pwd):
        print("✅ Válida")
    else:
        diagnosticar_password(pwd)