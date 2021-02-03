lista = list()
pares = list()
impar = list()
while True:
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)
    lista.append(n)
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(f'A sua lista foi {lista}\nVoce digitou {pares} numeros pares\nE digitou {impar} numeros impares')