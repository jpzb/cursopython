"""
Dictionary Comprehension

Pense no seguinte:

Se quisermos crirar uma lista, fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4) # 1, 2, 3, 4

Se quisermos criar um set:

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Síntaxe

{chave:valor for valor in iterável}
[valor for valor in iterável]

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor ** 2 for valor in numeros}

print(quadrado)

chave = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chave[i]: valores[i] for i in range(0, len(chave))}
print(mistura)
"""

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
