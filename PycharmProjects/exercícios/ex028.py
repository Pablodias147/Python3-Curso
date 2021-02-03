import random
print('x=x'* 17)
print('Vou pensar em um número entre 0 a 10, tenta acertar')
print('x=x'* 17)
p = int(input('Digite um número:'))
r = random.randint(0, 10)
if p == r:
    print('Parabens voce acertou')
else:
    print('Você errou')