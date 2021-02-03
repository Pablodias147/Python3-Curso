casa = float(input("Qual o valor da casa?"))
salario = float(input("Qual o seu salario?"))
anos = int(input("em quantos anos voce vai pagar a casa?"))
minimo =  (30 * salario / 100)
prestação  = casa / (anos % 12)
if prestação <= minimo:
    print("o emprestimo foi negado")
else: print("seu emprestimo foi aceito")
