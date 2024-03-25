"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios.
"""

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

# OBS: Não confunda a função random() com o pacote random.
