from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento:"))
idade = atual - nasc
print("quam basceu em {} tem {} anos em {}".format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar imediatamente")
elif idade < 18:
    saldo = idade - 18
    print("Você ainda nao tem 18 anos faltam {} para voce se alistar".format(saldo))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print("Voce ja deveria ter se alistar há {} anos".format(saldo))
    print("Seu ano de alistamento foi em {}".format(ano))
