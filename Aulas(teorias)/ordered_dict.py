"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elementos não é garatida
dicionario = {"a": 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print(dicionario)

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f"Chave = {chave}, valor = {valor}")

"""

from collections import OrderedDict
# Entendendo a diferença entre Dict e OrderedDict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 2, 'b': 1}

print(dict1 == dict2) # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'a': 2, 'b': 1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para o OrderedDict

