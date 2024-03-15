"""
O block try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo, assim,
que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // Execução problemática
except:
    // O que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    funcao()
except:
    print("Deu algum problema")

# Tente executar a função funcao(), caso você encontre erros, imprima a mensagem de erro.

# OBS: Tratar erro de forma genérica, não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de forma
específica

# Exemplo 2 - Tratando um erro específico

try:
    funcao()
except NameError:
    print("Você está utilizando uma função inexistente")

# Exemplo 3 - Tratando um erro específico

try:
    len(4)
except NameError:
    print("Você está utilizando uma função inexistente")

# Exemplo 4 - Tratando um erro específico com detalhes do erro

try:
    len(4)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    print("String"[9])
    # len(4)
    # func()
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err:
    print(f"Deu TypeError: {err}")
except:
    print("Deu erro diferente")
"""

def pega_valor(dic, chave):
    try:
        return dic[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "João"}

print(pega_valor(dic, "chave"))
print(pega_valor(4, "nome"))
