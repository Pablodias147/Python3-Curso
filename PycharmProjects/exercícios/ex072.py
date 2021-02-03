cont = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'oito', 'Nove', 'Dez')
while True:
    num = int(input("Digite um numero de 0 ate 10:"))
    if 0 <= num <= 20:
        break
    print("Tente Novamente! ", end="")
print(f"Voce digitou o numero {cont[num]}")