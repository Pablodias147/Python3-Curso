from datetime import date
atual = date.today().year
nas = int(input("qual o ano que voce nasceu?"))
idade = atual - nas
print(idade)
if idade <= 9:
    print("Sua categoria é MIRIM")
elif idade >= 10 and idade <= 14:
    print("Sua categoria é INFANTIL")
elif idade >= 15 and idade <=19:
    print("Sua categoria é JUNIOR")
elif idade == 20:
    print("Sua categoria é SENIOR")
elif idade > 19:
    print("Sua categoria é MASTER")
