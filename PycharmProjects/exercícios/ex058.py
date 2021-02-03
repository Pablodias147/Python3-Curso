from random import randint
random = randint(1, 10)
tot = 0
chute = int(input("O computador pensou em um numero de 0 a 10, tente adivinhar:"))
while chute != random:
    chute = int(input("Voce errou! tente novamente:"))
    tot += 1
print("PARABENS voce acertou!\nO numero que o computador pensou foi {}\nO acertou em {} tentativas".format(random, tot))

