peso = float(input("Qual o seu peso?"))
altura = float(input("qual a sua altura?"))
imc = peso / (altura**2)
if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print("Esta no peso ideal")
elif imc >= 25.1 and imc <= 30:
    print("Voce esta com sobrepeso")
elif imc >= 30.1 and imc <= 40:
    print("Voce esta em obsidade")
else:
    imc > 40.1
    print("obsidade mormita ")
print(imc)