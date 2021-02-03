cont = 0
lista = list()
while True:
    lista.append(int(input("Digite um numero: ")))
    cont += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar?[S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print("~="* 10)
print(f"Voce digitou {cont} valores")
print("~="* 10)
lista.sort(reverse= True)
print(f'a lista na ordem descresente são {lista}')
if 5 in lista:
    print("O valor 5 ta na lista")
else:
    print("Nao tem o numero 5 na lista")