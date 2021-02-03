from datetime import date
tempo = date.today().year
totmaior = 0
totmenor = 0
for quan in range(0, 8):
    nas = int(input('Qual o ano de seu nascimento:'))
    idade = tempo - nas
    if idade >= 21:
     totmaior += 1
    else: totmenor += 1
print("ao todo tivemos {} de maiores de idade\nE tambem {} pessoas menor de idade".format(totmaior, totmenor))
