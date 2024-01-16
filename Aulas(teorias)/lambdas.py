"""
Utilizando Lambdas

Conhecidas como Expressões Lambdas, ou simplismente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão Lambda?
calc = lambda x: 3* x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressambdões las com múltiplas entradas

nome = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()

print(nome("roberto", "carlos"))

# Em funções Python, podemos ter nenhuma ou várias entradas. Em lambdas também.

amar = lambda : "Como não amar Python?"

print(amar())

# OBS: Se passarmos mais argumentos do que parâmetro esperados, teremos TypeError.

# Função quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def funcao_quad(a, b, c):
    Retorna a função f(x) = a * x ** 2 + b * x + c
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quad(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(funcao_quad(3, 0, 1)(2))

"""
