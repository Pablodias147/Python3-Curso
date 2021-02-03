from datetime import date
atual = date.today().year
pessoas = dict()
pessoas["nome"] = str(input("Nome: "))
pessoas["idade"] = atual - int(input("ano de nascimento: "))
pessoas['ctps'] = int(input("Carteira de trabalho:[0 não tem] "))
if pessoas['ctps'] != 0:
    pessoas["contratação"] = int(input("Ano de contratação: "))
    pessoas["salario"] = float(input("Salario: R$"))
    pessoas["Aposentadoria"] = pessoas["idade"] + ((pessoas["contratação"] + 35) - atual)
for c, v in pessoas.items():
    print(f"{c} tem o valor {v}")