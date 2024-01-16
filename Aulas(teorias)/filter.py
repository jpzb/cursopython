"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(media)

# OBS: Assim como a função map(), a filter recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter, eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)  # Mesma coisa que lambda x: x != '' ou lambda x: len(x) > 0

print(list(res))

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada
# elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
# de acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": 'samuel', 'tweets': ['Eu adoro bolos', "Eu adoro pizzas"]},
    {"username": 'carla', 'tweets': ["Eu amo meu gato"]},
    {"username": 'jeff', 'tweets': []},
    {"username": 'bob123', 'tweets': []},
    {"username": 'doggo', 'tweets': ['Eu gosto de cachorros', "Vou sair hoje"]},
    {"username": 'gal-sal', 'tweets': []}
]

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativo = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2
inativo = list(filter(lambda u: not u['tweets'], usuarios))
print(inativo)
"""

# Como combinar filter() e map()

nomes = ["Vanessa", "Ana", "Maria"]

# Devemos criar uma lista contendo "Sua instrutora é" + nome, desde que cada nome tenha menos de 5 caractéres

lista = list(map(lambda nome: f"Sua instrutora é {nome}", filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
