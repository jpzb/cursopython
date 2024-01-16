"""
PEP8 - Python Enhancement Proposals
são propostas de melhorias para a linguagem python
 The Zen of Python
import this
A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar= 5

[3] - Utilize quatro espaços para identação! (Não use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco.
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# Errado
import sys, os

# Certo
import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types imports (
    StringType
    ListType
    SetType
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de contanstes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo[ 1 ], outro{ 2 } )

# Faça:

funcao(algo[1], outro{2})

# Não faça:

algo (1)

# Faça:

algo(1)

[7] - Termine sempre uma instrução com uma nova linha
"""
