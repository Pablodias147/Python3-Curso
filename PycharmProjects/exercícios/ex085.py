listagem = [[], []]
for p in range(0, 7):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        listagem[0].append(n)
    else:
        listagem[1].append(n)

print(f"Os numeros pares digitados foram {sorted(listagem[0])}")
print(f"Os numeros impares digitados foram {sorted(listagem[1])}")