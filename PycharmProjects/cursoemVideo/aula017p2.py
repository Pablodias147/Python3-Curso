galera = [["Pablo", 17], ["Milena", 4], ["Leandra", 14], ["Paloma", 24]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")

pessoas = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input("Nome? ")))
    dados.append(int(input("Idade? ")))
    pessoas.append(dados[:])
    dados.clear()

for r in pessoas:
    if r[1] >= 21:
        print(f"{r[0]} É maior de idade")
    else:
        print(f"{r[0]} é menor de idade")