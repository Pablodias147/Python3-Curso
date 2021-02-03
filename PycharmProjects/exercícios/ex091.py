from random import randint
from time import sleep
from operator import itemgetter
jogo = {"jogador1": randint(1, 6),
        "jogador2": randint(1, 6),
        "jogador3": randint(1, 6),
        "jogador4": randint(1, 6)}
ranking = list()
print("Valores sorteados: ")
for k, v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.75)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print("RANKING DOS JOGADORES!")
print()
for v, c in enumerate(ranking):
    print(f"{v + 1} lugar: {c[0]} com {c[1]}")
    sleep(0.75)