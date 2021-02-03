r = "S"
par = impar = 0
while r == "S":
    n = int(input("Digite um valor:"))
    r = str(input("Quer continuar? [S/N]")).upper()
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print("Voce digitou {} numeros PARES e {} IMPARES".format(par, impar))