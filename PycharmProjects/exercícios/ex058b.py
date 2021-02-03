from random import randint
computador = randint(0, 10)
print("Seu computador pensou em um numero de 0 a 10 tente adivinhar")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Tente advinhar:"))
    palpites += 1
    if jogador == computador:
        acertou = True
print("Acertou\nVoce consegui em {} tentativas".format(palpites))
