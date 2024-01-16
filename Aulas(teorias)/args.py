"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já, lembre-se que tuplas são imutáveis.

# Exemplos


def soma(n1=1, n2=2, n3=3):
    return n1 + n2 + n3


print(soma(4, 6, 9))

print(soma(4, 6))

# Entendendo o *args


def soma(nome, email, *args):
    print(sum(args))


soma("Angelina", "Jolie")
soma("Angelina", "Jolie", 1)
soma("Angelina", "Jolie", 1, 2)
soma("Angelina", "Jolie", 1, 2, 3)
soma("Angelina", "Jolie", 1, 2, 3, 4)
soma("Angelina", "Jolie", 23.4, 12.5)

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem-vindo Geek!"
    return "Eu não tenho certeza quem você é..."


print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.145))

"""


def soma(*args):
    return sum(args)


print(soma())
print(soma(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos
# passamos como argumento uma coleção de dados. Desta forma, ele saberá
# que precisará antes, desempacotar estes dados.