from random import randint
vitoria = 0
print("=-"* 12)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-"* 12)
while True:
    computador = randint(0, 10)
    jogador = int(input("Diga um valor:"))
    total = jogador + computador
    tipo = " "
    while tipo not in "PpIi":
        tipo = str(input("Par ou impar? [P/I]")).strip().upper()[0]
    if tipo == "P":
        if total % 2 == 0:
            print("Voce ganhou!!!!!!!!")
            print(f"O computador jogou {computador} e voce {jogador}")
            vitoria += 1
        else:
            print("Voce perdeu!")
            print(f"O computador jogou {computador} e voce {jogador}")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Voce Ganhou!!!!!!")
            print(f"O computador jogou {computador} e voce {jogador}")
            vitoria += 1
        else:
            print("VOCE PERDEU!")
            print(f"O computador jogou {computador} e voce {jogador}")
            break
    print("Vamos jogar novamente...")

print(f"GAMER OVER! Voce ganhou {vitoria} vex")