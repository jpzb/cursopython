"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas
normalmente ainda é utilizado para manter compatibilidade.

from pacote import teste1, teste2
from pacote.subpacote import teste3, teste4

print(teste1.funcao1(12, 3))
print(teste1.pi)

print(teste2.funcao2())
print(teste2.time)

print(teste3.funcao3())
print(teste4.funcao4())

from pacote.teste1 import funcao1
from pacote.subpacote.teste4 import funcao4

print(funcao1(6, 9))
print(funcao4())

"""
