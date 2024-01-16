n = int(input())

lista = [int(input()) for i in range(n)]
primeiro = True
for j in lista:
    if j == 0 and primeiro:
        lista.remove(lista[lista.index(j) - 1])
        lista.remove(j)
        primeiro = False
    if not primeiro:
        lista.remove(j)
        lista.remove(lista)

print(lista)
print(sum(lista))

"""
10
1
3
5
4
0
0
7
0
0
6

4
3
0
4
0
"""
