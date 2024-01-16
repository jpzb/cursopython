"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução
do nosso código.

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.

# Exemplos de SyntaxError

a)
def funcao:
    print("SyntaxError")

b)
None = 1

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida

# Exemplos NameError

a)
print(teste)

b)
teste()

c)
a = 8

if a > 10:
    msg = "Maior q 10"

print(msg)

3 - TypeError -> Ocorre quando uma operação, função ou ação é aplicada a um tipo errado.

# Exemplos TypeError

a)
print(len(5))

b)
print("String" + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um índice inválido.

# Exemplos de IndexError

a)
lista = [1, 2]
print(lista[2])

b)
lista = [1, 2]
print(lista[0][1])

5 - ValueError -> Ocorre quando uma função ou operação built-in (integrada) recebe um argumento com tipo correto,
mas valor inapropriado.

# Exemplos ValueError

a)
print(int("String"))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

# Exemplos KeyError

a)
dic = {}
print(dic["Chave"])

7 - AttributeError -> Ocorre quando uma variável não tem um aributo ou função.


# Exemplos AttributeError

a)
tupla = (11, 2, 33, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError

a)
def nova():
print("String")

b)
for i in range(1):
print(i)
"""

