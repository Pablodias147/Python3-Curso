total = mais1000 = cont = menor =0
barato = ""
while True:
    nome = str(input("Digite o nome do produto:"))
    preço = float(input("O valor:"))
    total += preço
    cont += 1
    if preço > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print("========Processo Finalizado========")
print(f"o total gasto na compra foi {total}\nteve {mais1000} produtos que custo mais de R$1.000 reais\nO nomes do produto mais baratos foi {barato}")
