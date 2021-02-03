lista = list()
maior = menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Na posição {c} o valor:")))
    if c ==0:
        maior = menor = lista[c]
    else:
        if lista[c] >maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f"Voce digitou os valores {lista}")
print(f'o maior numero digitado foi {maior} e esta na posição ', end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}", end="...")
print(f'\no menor numero digitado foi {menor} e esta na posição ', end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}", end="...")
