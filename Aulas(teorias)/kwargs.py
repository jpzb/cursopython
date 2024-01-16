"""
**kwargs

Poderíamos chamar esse parâmetro de **xix, mas por convenção, chamomos de **kwargs

Este é só mais um parâmetro, mas diferente do *args, que coloca os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses
parâmetros extras em um dicionário.

# Exemplo

def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")


cores(marcos="verde", julia="amarelo", fernanda="azul", vanessa="branco")

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores()
cores(geek="navy")

# Exemplo mais complexo

def cumprimento_especia(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == "Python":
        return "Você recebeu um cumprimento Pythônico Geek!"
    elif "geek" in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não tenho certeza quem você é..."


print(cumprimento_especia())
print(cumprimento_especia(geek="Python"))
print(cumprimento_especia(geek="Oi"))
print(cumprimento_especia(geek="Especial"))

# Nas nossas funções, podemos ter (NESTA ORDEM):

# - Parâmetros obrigatórios;
# - *agrs;
# - Parâmetros default (não obrigatórios);
# - **kwargs;


def minha_f(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("Casado")
    else:
        print("Solteiro")
    print(kwargs)


minha_f(8, "Julia")
minha_f(18, "Felicity", 4, 5, 3, solteiro=True)
minha_f(34, "Felipe", eu="Não", voce="Vai")
minha_f(19, "Carla", 9, 4, 3, java=False, python=True)

# Entendendo por quê é importante manter a ordem dos parâmetros na declaração


# Função com a ordem correta de parâmetros
# def mostra(a, b, *args, instrutor='Geek', **kwargs):
#     return [a, b, args, instrutor, kwargs]

# Função com a  ordem incorreta de parâmetros
def mostra(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra(1, 2, 3, sobrenome="Univeristy", cargo='Instrutor'))


# Desenpacotar com **kwargs


def mostra(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Felicity', 'sobrenome': "Jones"}

print(mostra(**nomes))
"""


def soma(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
soma(1, 2, 3)
soma(*lista)

dicio = dict(a=1, b=2, c=3)
soma(**dicio)

# OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função
