one = float(input('qual e  o comprimeito do cateto oposto:'))
two = float(input('qual o comprimento do cateto adjacente:'))
tri = (one ** 2 + two ** 2) ** (1/2)
print('Cateto oposto:{} Cateto adjacante:{} A hipotenusa sera:{}'.format(one, two, tri ))
