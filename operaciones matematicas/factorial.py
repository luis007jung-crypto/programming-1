def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

print(factorial(3))
print(factorial(5))
print(factorial(6))