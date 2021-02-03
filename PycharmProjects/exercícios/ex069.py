
mais18 = homem_cadastrado = menos20 =0
while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade > 18:
        mais18 += 1
    if sexo == "M":
        homem_cadastrado += 1
    if idade < 20 and sexo == "F":
        menos20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print("========FIM DO PROGRAMA=======")
print(f"Total de pessoas com mais de 18 anos:{mais18}")
print(f"Ao todo tivemos {homem_cadastrado} homes cadastrados")
print(f"E tivemos {menos20} Mulher com menos de 20 anos")
