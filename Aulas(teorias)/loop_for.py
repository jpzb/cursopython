"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
- String
- Lista
- Range

# Exemplo de for 1: (Iterando em uma string)
for letra in nome:
    print(letra)
    
# Exemplo de for 2: (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exmemplo de for 3: (Iterando sobre um range)

range(valor inicial, valor final)
Obs: o valor final não é incluso.

for numero in range(0, 10):
    print(numero)

Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), ...)

for i, v in enumerate(nome):
    print(nome[i])

for _, letra in enumerate(nome):
    print(letra)
Obs: quando não precisamos de um valor, podemos descarta-lo usando underline (_)

for valor in enumerate(nome):
    print(valor)   # valor[0] -> traz os índices e valor[1] -> traz as letras
Obs: traz tudo


nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
# Temos que transformar em uma lista

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma = soma + num
print(f"A soma é {soma}")

nome = "Geek University"

for letra in nome:
    print(letra, end='') # Sem pular linha

for _ in range(3):                     Original: U+1F60D
    for num in range(1, 11):           Modificado: U0001F60D
        print('\U0001F60D' * num)
Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""