pessoas = list()
dados = list()
cont = 0
maior_peso = 0
menor_peso = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    cont += 1
    pessoas.append(dados[:])
    dados.clear()
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar?[S/N] ")).strip().upper()[0]

    if continuar == "N":
        print("Programa Finalizado")
        break

print(f"Ao todo voce cadastrou {cont} pessoas")
print(f'o maior peso foi de {maior_peso}KG', end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}]")
print(f"o menor peso foi de {menor_peso}KG", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}]")