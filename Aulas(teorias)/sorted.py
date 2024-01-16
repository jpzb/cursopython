"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() server para ordenar.

OBS: O sorted sempre retorna uma lista com os elementos do iterável ordenado.

# Exemplo

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

# Adicionando parâmetros ao sorted()

numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas.

usuarios = [
    {"username": 'samuel', 'tweets': ['Daylight demon é o mais pika', "H4k3d by 4ng3l 0f th3 n1gth"]},
    {"username": 'carla', 'tweets': ["Eu amo meu gato"]},
    {"username": 'jeff', 'tweets': []},
    {"username": 'bob123', 'tweets': [], "cor": "Preto"},
    {"username": 'doggo', 'tweets': ['Eu gosto de cachorros', "Vou sair hoje"]},
    {"username": 'gal-sal', 'tweets': ["Kian Sabe"], "cor": "Amarelo", "elemento": "Conhecimento"}
]

print(usuarios)

# Ordenado por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["tweets"], reverse=True))

"""

# Último exemplo

musicas = [
    {"titulo": "Master of Puppets", "tocou": 100},
    {"titulo": "Heat waves", "tocou": 20},
    {"titulo": "A Man Whitout Love", "tocou": 45}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))
