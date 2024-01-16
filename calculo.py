s = int(input())
a = int(input())
b = int(input())

cont = 0
for i in range(a, b + 1):
    lista_numero = [int(i) for i in str(i)]
    if sum(lista_numero) == s:
        cont += 1

print(cont)
