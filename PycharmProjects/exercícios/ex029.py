velocidade = float(input("Qual a velocidade do seu carro ?"))
if velocidade > 80:
    print("VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE DE 80KM/H")
    multa = (velocidade - 80) * 7
    print("Sua multa é de {}".format(multa))
else: print('Tenha um bom dia, Diriga com segurança')
