"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi : {receita[chave]}')

# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores

print(receita.values())

for valores in receita.values():
    print(valores)

# Desenpacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""
