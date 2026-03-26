import math

def area_circulo(radio):
    return math.pi * radio ** 2

print(area_circulo(1))
print(area_circulo(3))
print(area_circulo(5))


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(es_primo(2))
print(es_primo(10))
print(es_primo(17))


def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(factorial(3))
print(factorial(5))
print(factorial(6))


def fibonacci(n):
    lista = []
    a, b = 0, 1
    for i in range(n):
        lista.append(a)
        a, b = b, a+b
    return lista

print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(10))


def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_a_fahrenheit(0))
print(celsius_a_fahrenheit(25))
print(celsius_a_fahrenheit(100))


def maximo(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

print(maximo([1,2,3]))
print(maximo([10,5,8]))
print(maximo([-1,-5,-3]))

