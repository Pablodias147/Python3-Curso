from random import randint
from time import sleep
print("Suas opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura")
jogador = int(input("Qual vai ser sua jogada?"))
print("JO")
sleep(0.75)
print("KEN")
sleep(0.75)
print("PO")

itens = ("pedra", "papel", "tesoura")
computador = randint(1, 2)
print("-=-" * 10)
print("o computador escolheu {}".format(itens[computador]))
print("O jogador escolheu {}".format(itens[jogador]))
print("-=-" * 10)
if computador == 0:#computaddor jogou pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("VOCÊ GANHOU!!\nPAPEL GANHA DE PEDRA")
    elif jogador == 2:
        print("O computador ganhou!\nPedra ganha de tesoura")
elif computador == 1:           #computaddor jogou papel
    if jogador == 0:
        print("O computador ganhou!\nPapel ganha de pedra")
    elif jogador == 1:
        print("EMPATE!!")
    elif jogador == 2:
        print("VOCÊ GANHOU!!!\nTsoura ganha de papel")
elif computador == 2:          #computaddor jogou tesoura
    if jogador == 0:
        print("VOCÊ GANHOU!\nPedra ganha de tesoura")
    elif jogador == 1:
        print("O computador ganhou!!\nTesoura ganha de papel")
    elif jogador == 2:
        print("EMPATE!!")