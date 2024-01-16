alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "x", "z"]
vogais = ["a", "e", "i", "o", "u"]

p = input()
palavra_nova = ""


for i in p:
    palavra_nova += i
    if i not in vogais:
        for j in range(1, 4):
            if alfabeto[alfabeto.index(i) - j] in vogais:
                palavra_nova += alfabeto[alfabeto.index(i) - j]
                break
            else:
                try:
                    if alfabeto[alfabeto.index(i) + j] in vogais:
                        palavra_nova += alfabeto[alfabeto.index(i) + j]
                        break
                except IndexError:
                    continue
        try:
            if alfabeto[alfabeto.index(i) + 1] not in vogais:
                palavra_nova += alfabeto[alfabeto.index(i) + 1]
            else:
                palavra_nova += alfabeto[alfabeto.index(i) + 2]
        except IndexError:
            palavra_nova += i

print(palavra_nova)
