"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer os ranges para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequêcias numéricas, não de forma aleatória,
mas sim de maneira específica.

Formas Gerais:

# Forma 1
range(valor_de_parada)

Obs: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor_de_início, valor_de_parada)

Obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3
range(valor_de_início, valor_de_parada, passo)

Obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4
range(valor_de_início, valor_de_parada, passo)

Obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)
"""
