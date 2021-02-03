numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! não vou adiciopnar")
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print("-="*20)
print(f'Os valores adicionados foram {sorted(numeros)}')