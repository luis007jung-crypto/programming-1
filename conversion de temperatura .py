def convertir(valor, origen, destino):
    if origen == 'F':
        valor = (valor - 32) * 5/9
    elif origen == 'K':
        valor = valor - 273.15

    # ahora ya está en C

    if destino == 'F':
        return valor * 9/5 + 32
    elif destino == 'K':
        return valor + 273.15
    elif destino == 'C':
        return valor    