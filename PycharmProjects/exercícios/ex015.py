a = float(input('Quantos dias  alugados? '))
b = float(input('Quantos Km rodados? '))
c = a * 60
d = b * 0.15
e = c + d
print('O total a  pagar é de R${:.2f}'.format(e))
