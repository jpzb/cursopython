"""
Min e Max

max() -> Retorna o maior valor em um iterável ou maior de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = 1, 8, 4, 99, 34, 129
print(max(tupla))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'f': 324, 'e': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

# Faça um programa que receba 2 valores de um usuário e mostre o maior

var1 = int(input("Informe o primerio valor: "))
var2 = int(input("Informe o segundo valor: "))

print(max(var1, var2))

print(max(4, 67, 54, 12))

print(max('a', 'b', 'c', 'd', 'e', 'f'))

print(max(21.22, 123.22))

print(max("Cassino Sabadasso"))

min() -> Retorna o menor valor em um iterável ou menor de dois ou mais elementos.

# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = 1, 8, 4, 99, 34, 129
print(min(tupla))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'f': 324, 'e': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

# Faça um programa que receba 2 valores de um usuário e mostre o maior

var1 = int(input("Informe o primerio valor: "))
var2 = int(input("Informe o segundo valor: "))

print(min(var1, var2))

print(min(4, 67, 54, 12))

print(min('a', 'b', 'c', 'd', 'e', 'f'))

print(min(21.22, 123.22))

print(min("Cassino-Sabadasso"))

# Outros exemplos

nomes = ['Arya', 'Samson', 'Dara', 'Tim', 'Cassiano', 'Eduarda', 'Hugo Neneca', 'Hugo']

print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

"""

musicas = [
    {"titulo": "Master of Puppets", "tocou": 100},
    {"titulo": "Heat waves", "tocou": 20},
    {"titulo": "A Man Whitout Love", "tocou": 45}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Desafio! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

# Desafio! Como encontrar a música mais tocada e menos tocada sem usar max(), min() e lambda?

max = 0, ''
min = 1000, ''
for i in musicas:
    if i["tocou"] > max[0]:
        max = i['tocou'], i['titulo']
    if i["tocou"] < min[0]:
        min = i['tocou'], i['titulo']

print(max[1], min[1])
