print("\033[0;33mVocê vai escrever dois numeros inteiros e vou dizer qual vai ser o maior e o menor\033[m")
num1 = int(input("Escreva o primeiro numero:"))
num2 = int(input("Escreva o segundo numero:"))
if num1 > num2:
    print("o primeiro numero é maior")
elif num2 > num1:
    print("o segundo numero é maior")
elif num1 == num2:
    print("os numeros sao iguais espertinho")
else: print("erro, tente novamente")

