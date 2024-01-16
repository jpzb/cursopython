"""
Recebendo dados de usários
"""
# Entrada de dados
# Dois jeitos de receber dados
# print("Informe seu nome")
# nome = input()
nome = input("Informe seu nome: ")

# Exemplo de print 'antigo' 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print("Seja bem vindo(a) {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')
# print("Qual a sua idade? ")
# idade = input()

idade = int(input("Informe sua idade: "))

# Saída de dados
# print("{0} tem {1} anos de idade".format(nome, idade))
print(f'{nome} tem {idade} anos de idade.')
print(f'{nome} nasceu em {2021 - idade}')
