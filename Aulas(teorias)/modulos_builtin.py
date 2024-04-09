"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

# Constumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import (
    randint,
    random,
    choice
)

print(random())
print(randint(5, 89))
print(choice("Flamengo"))
"""

