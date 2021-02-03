cont = soma = 0
exite = False
print("Digite 999 para sair")
while not exite:
    num = int(input("Digite um numero:"))
    if num != 999:
        soma += num
        cont += 1
    if num == 999:
        exite = True

print("Voce digitou {} numeros. a soma entre eles foram {}".format(cont, soma))
print("FIM")