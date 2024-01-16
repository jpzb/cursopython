"""
# 1
num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

if num1 > num2:
    print(f"O primeiro valor: {num1} é maior que o segundo: {num2}")
else:
    print(f"O segundo valor: {num2} é maior que o primeiro: {num1}")

# 2
num1 = int(input("Informe um valor: "))

if num1 > 0:
    num1 = num1 ** (1/2)
else:
    print("Número inválido")
print(num1)

# 3
num1 = float(input("Informe um número real: "))

if num1 > 0:
    num1 = num1 ** (1/2)
else:
    num1 = num1 ** 2
print(num1)

# 4
num1 = int(input("Informe um valor: "))

if num1 > 0:
    pot = num1 ** 2
    raiz = num1 ** (1/2)
    print(pot, raiz)

# 5
num1 = int(input("Informe um valor: "))

if num1 % 2 == 0:
    print(f"Valor par: {num1}")
else:
    print(f"Valor ímpar: {num1}")

# 6
num1 = int(input("Informe um valor para o primeiro número: "))
num2 = int(input("Informe um valor para o segundo número: "))

if num1 > num2:
    dif = num1 - num2
    print(f"O maior é {num1} e a diferênça é {dif}")
else:
    dif = num2 - num1
    print(f"O maior é {num2} e a diferênça é {dif}")

# 7
num1 = int(input("Informe um valor para o primeiro número: "))
num2 = int(input("Informe um valor para o segundo número: "))

if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
elif num1 == num2:
    print("Números iguais")

# 8
nota = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

if 0.0 <= nota <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota + nota2) / 2
    print(media)
else:
    print("Nota inválida.")

# 9
salario = float(input("Informe seu salário: "))
prestacao = float(input("Informe sua prestação: "))

if prestacao > (salario * 20) / 100:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")

# 10
altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo m/f: ")

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal}")
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal}")
elif 'F' != sexo.upper() != 'M':
    print("Sexo inválido.")
"""
