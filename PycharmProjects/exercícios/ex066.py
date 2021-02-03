cont = 0
soma = 0
print("Digite 999 para parar")
while True:
    num = int(input("Digite um numero inteiro:"))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"a soma entre os {cont} valores é {soma}")