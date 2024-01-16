def primeira():
    for n in range(1, 6):
        print(n * 3)
    return 0


def seg():
    for n in range(1, 101):
        print(n)
    m = 1
    while m < 101:
        print(m)
        m = m + 1
    o = 1
    while o < 101:
        if o == 101:
            break
        else:
            print(o)
            o = o + 1
    return 0


def ter():
    contreg = 10
    while contreg > -1:
        if contreg > 0:
            print(contreg)
        else:
            print("Fim")
        contreg = contreg - 1
    return 0


def qrt():
    vlr = 0
    while vlr < 100001:
        print(vlr)
        vlr = vlr + 1000
    return 0


def qnt():
    lista = []
    for n in range(0, 10):
        lista.append(int(input("Informe um valor: ")))
    print(sum(lista))
    return 0


def sex():
    lista = []
    for n in range(0, 10):
        lista.append(int(input("Informe um valor: ")))
    print((sum(lista)) // len(lista))
    return 0


def seti():
    lista = []
    for n in range(0, 10):
        lista.append(int(input("Informe um valor: ")))
        print(lista)
        if n < 0:
            lista.pop(-1)
            print(lista)
    print((sum(lista)) // len(lista))
    return 0


if __name__ == '__main__':
    seti()
