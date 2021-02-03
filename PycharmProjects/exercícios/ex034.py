salario = float(input("Qual o seu salario:"))
if salario > 1250.:
     novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)
print("seu aumento vai ser de: {}".format(novo))