def main():
    n = int(input())
    amigos = []

    for i in range(n):
        amigos.append([input().upper(), int(input())])

    saida = []

    chave = 0
    for i in amigos:
        tempo = 0
        if i[0] == "R":
            chave = i[1]
            for j in range(amigos.index(i), len(amigos)):
                # [['R', 2], ['R', 3], ['T', 5], ['E', 2], ['E', 3]]
                match amigos[j][1]:
                    ca
                if amigos[j][1] != chave:
                    if amigos[j][0] != "T":
                        if amigos[j - 1][0] != "T":
                            tempo += 1
                    else:
                        tempo += amigos[j][1]
                else:
                    if amigos[j][0] == "E":
                        if amigos[j - 1][0] != "T" and (j - 1) >= 0:
                            tempo += 1
                        break
            saida.append([chave, tempo])

    print(saida)
    print(amigos)
"""
5
r
2
r
3
t
5
e
2
e
3


r 2
r 3
t 5 
e 2
e 3

14
R
12
T
2
R
23
T
3
R
45
E
45
R
45
E
23
R
23
T
2
E
23
R
34
E
12
E
34
"""

if __name__ == "__main__":
    main()
