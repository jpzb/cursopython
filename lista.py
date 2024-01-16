n = int(input())
lista = list(map(int, input().split()))

i = 0
j = n - 1
cont = 0
soma_esquerda = lista[i]
soma_direita = lista[j]

while i <= j:
    if soma_esquerda == soma_direita:
        i += 1
        j -= 1
        soma_esquerda = lista[i]
        soma_direita = lista[j]
    elif soma_esquerda < soma_direita:
        i += 1
        soma_esquerda += lista[i]
        cont += 1
        if i == j:
            break
    else:
        j -= 1
        soma_direita += lista[j]
        cont += 1
        if i == j:
            break

print(cont)
