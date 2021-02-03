num = (int(input("Digite um numero: ")), int(input("Digite outr numero: ")), int(input("Digite mais um numero: ")),
       int(input("Digite o ultimo numero: ")))
print(f"Os numeros digitados foram {num}")
print(f"O numero 9 apareceu {num.count(9)} vezes ")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+ 1} posição")
print("Os valores pares digitados foram: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=", ")