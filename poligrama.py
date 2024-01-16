n = int(input())
p = input()

primeira = p[:n//2]
segunda = p[n//2: n]
lista1 = [i for i in primeira]
lista2 = [i for i in segunda]

lista1.sort()
lista2.sort()

if lista1 == lista2:
    print(primeira)
else:
    print("*")
# https://www.youtube.com/watch?v=MmUMKmnToIs
