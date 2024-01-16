"""
Listas (list)

Listas em Python funcionam como vetores/matrizes (arrays, em outras linguagens), com a diferença
de serem DINÂMICOS e de também podermos colocar QUALQUER tipo de dado.

Linguagens C/Java:
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens, se você criar um array do tipo int e com tamnho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos checar se determinado valor está contido na lista
num = int(input("Informe um valor: "))
if num in lista4:
    print(f"Encontrei o número {num}")
else:
    print(f"Não encontrei o número {num}")

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrência de um valor em uma lista.
print(lista1.count(1))
print(lista5.count('e'))

# Podemos adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista.")
else:
    print("Não encontrei a lista.")

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional à lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.inset(2, 'Novo Valor')
print(list1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1, lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista2))

# Podemos facilmente remover o último elemento de uma lista
# OBS: o pop não somente remove o último elemento como também retorna
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: os elementos da direita deste índice serão deslocados para a esquerda
# OBS: se não houve elemento no índice informado, teremos um erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente uma string para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]

# Iterando sobre listas

# Exemplo 1 - Utilizando for

for elemento in lista1:
    print()

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''
while produto != 'sair':
    print("Adicione um produto ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 5
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso as elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde o
# final de um elemento está ligado ao início da lista

print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
# print(cores[-5]) erro

for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar índice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
print(lista)

# Outros métodos não tão importantes, mas também úteis

# Encontrar um índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
print(numeros.index(6))
print(numeros.index(9))

# OBS: Caso não tenha esse elemento na lista, será apresentado erro ValueError
# OBS: Retorna o índice do primeiro elemento informado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # Buscar o valor 5 a partir do índice 1
# OBS: Caso não tenha esse elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, início/fim
print(numeros.index(8, 3, 6)) # Buscar o índice do valor 8 entre os índices de 3 a 6

# Revisão de slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

# Trabalhando com slice de lista com parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])

# Trabalhando com slice de lista com parâmetro 'fim'

print(lista[:2])
print(lista[:4])
print(lista[1:3])

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista[1::2])
print(lista[::2])

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desenpacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1, num2, num3)

# OBS: se tivermos um número diferente de elementos na lista ou variáveis para receber dados, teremos um ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista, nova)

# Ao utilizarmos a lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista, nova)

# Ao utilizarmos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy
"""
