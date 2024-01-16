"""
Len, Abs, Sum, Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Só pra revisar

print(len("Geel University"))

print(len({"a": 1, "b": 2}))

# Por debaixo dos panos, quando utilizamos a função len(), o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem sinal.

# Exemplos abs

print(abs(-4))
print(abs(5))
print(abs(-3.21))

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma dos elementos,
incluindo o valor inicial.

OBS: O valor inicial default = 0

# Exemplos sum

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.222, 3.8], 0.978))

# Round

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for
informada, retorna o inteiro mais próximo da entrada.

# Exemplo round

print(round(5.5))
print(round(1.32213132131, 2))
print(round(10.929, 2))

"""
