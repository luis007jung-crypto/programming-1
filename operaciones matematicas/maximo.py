def maximo(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor

print(maximo([1,2,3]))
print(maximo([10,5,8]))
print(maximo([-1,-5,-3]))