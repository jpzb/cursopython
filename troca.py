n, t = map(int, input().split())
lista_cima = list(map(int, input().split()))
lista_baixo = list(map(int, input().split()))

lista_combinada = lista_cima + lista_baixo

for _ in range(t):
    i, j = map(int, input().split())
    i -= 1
    lista_combinada[i:j], lista_combinada[n+i:n+j] = lista_combinada[n+i:n+j], lista_combinada[i:j]

lista_cima = lista_combinada[:n]
lista_baixo = lista_combinada[n:]

print(*map(str, lista_cima))
