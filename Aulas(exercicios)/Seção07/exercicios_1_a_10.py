def prim():
    a = [1, 0, 5, -2, -5, 7]
    soma = a[0] + a[1] + a[5]
    print(soma)
    a[4] = 100
    for valor in a:
        print(valor)
    return 0


def seg():
    lista = [int(input("?")), int(input("?")), int(input("?")), int(input("?")), int(input("?")), int(input("?"))]
    print(lista)
    return 0


if __name__ == '__main__':
    seg()
