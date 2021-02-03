exit = False
soma = cont = maior = 0
menor = 10000000
while not exit:
    num = int(input("Digite um valor inteiro:"))
    segui = str(input("Quer continuar [S/N]:"))
    soma += num
    cont += 1
    if segui in "Nn":
        exit = True
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma % cont
print("a media dos valores são {}".format(media))
print("O maior valor digitado foi {} e o menor foi {}".format(maior, menor))
print("Fim")