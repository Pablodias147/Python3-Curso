nome = str(input('qual é seu nome?'))
if nome == 'Pablo':
    print('Que nome lindo voce tem!')
else: print('seu nome é tao normal')
print('bom dia {}'.format(nome))
n1 = float(input('qual foi sua primeira nota?'))
n2 = float(input('qual foi sua segunda nota?'))
m = (n1 + n2)/2
print('sua nota  foi {:.1f}'.format(m))
if m >= 7.0:
    print('sua nota foi boa parabens')
else:
    print('sua nota foi ruim')
