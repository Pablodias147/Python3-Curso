import math
c1 = float(input('Digite  o Ângulo que  você deseja:'))
c2 = math.sin(math.radians(c1))
c3 = math.cos(math.radians(c1))
c4 = math.tan(math.radians(c1))
print('O Ângulo de {} tem o SENO de {:.2f}\nO Ângulo de {} tem o COSSENO de {:.2f}\nO Ângulo de {} tem o TANGENTE de {:.2f}'.format(c1, c2, c1, c3, c1, c4))
