soma = 0
cont = 0
for c in range(1, 7):
     num = int(input("digite o {} valor inteiro:".format(c)))
     if num % 2 == 0:
         soma +=  num
         cont += 1
print("Voce informou {} numeros PARES. È a soma entre eles é {}".format(cont, soma))
