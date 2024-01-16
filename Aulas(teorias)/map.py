"""
Map

Com map, fazemos mapeamento de valores para função.

import math


def area(raio):
    Calcula a área de um círculo com raio 'r'.
    return math.pi * (raio ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum

areas = []
for r in raios:
    areas.append(area(r))
print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com lambda

print(list(map(lambda raio: math.pi * (raio ** 2), raios)))

# OBS: Após utilizar a função map(), depois da primeira utilização do resultado, ele zera.

# Para fixar - Map

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Função: f(x)

# Utilizamos a função map(f, dados), onde map irá mapear cada elemento dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), ..., f(an)

"""

# Mais um exemplo

cidades = [("Berlin", 29), ('Cairo', 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tóquio", 27),
           ("Nova Iorque", 28), ("Londres", 22)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))
print(list(map(c_f, cidades)))
