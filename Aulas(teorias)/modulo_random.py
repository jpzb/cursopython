"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.

# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo (não recomendado).

import random

# random() -> Gera um número pseudo-aleatório entre 0 e 1.

# OBS: Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (ficarão em memória). Caso você saiba quais funções usar deste módulo,
# então esta não seria a maneira ideal de utilização.

print(random.random())

# Para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função, separados
# por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é
# apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função específica do módulo

from random import random

# No import acima, estamos falando: Do módulo random, importe a função random

for i in range(10):
    print(random())

# uniform() -> Gerar um número real pseduo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluído.

# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint

for i in range(6):
    print(randint(1, 61), end=", ")

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))

print(choice("String"))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

cartas = ["K", "Q", 'J', 'A', 2, 3, 4, 5, 6, 7]

print(cartas)
shuffle(cartas)
print(cartas)
"""

