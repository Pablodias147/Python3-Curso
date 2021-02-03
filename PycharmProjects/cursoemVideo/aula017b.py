valores = list()
valores.append(5)

for cont in range(0, 5):
    valores.append(int(input("Digite um valor:")))
for v, c in enumerate(valores):
    print(f'Na posição {v} encontrei o valor {c}')
print("Chegeui no final da lista")

a = [1, 4, 6, 8]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')