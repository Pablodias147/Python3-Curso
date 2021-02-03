distancia = float(input('qual a distancia da sua viagem em km:'))
if distancia < 200:
    q =  distancia * 0.50
    print("Sua viagem custara {}".format(q))
else:
    w = distancia * 0.45
    print("Sua viagem custara {}".format(w))
