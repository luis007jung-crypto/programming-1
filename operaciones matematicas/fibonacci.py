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