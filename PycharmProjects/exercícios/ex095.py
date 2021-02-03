time = list()
dados = dict()
partidas = list()

while True:
    dados.clear()
    dados["nome"] = str(input("Nome: "))
    tot = dados["partidas"] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
    partidas.clear()
    for c in range(dados["partidas"]):
        partidas.append(int(input(f"Quantos gols no {c + 1}º jogo: ")))
    dados["gols"] = partidas[:]
    dados["total"] = sum(partidas)
    time.append(dados.copy())
    while True:
        res = str(input("Dejesa continuar?[S/N] ")).upper()[0]
        if res in "SN":
            break
        print("ERRO! Responda S ou N")
    if res == "N":
        break
print("-=" * 30)
print('cod', end="")
for i in dados.keys():
    print(f'{i:<15}', end="")
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3}', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print('-'*30)
while True:
    busca = int(input("Mostrar dados de qual jogador:[999 para] "))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! Não existe jogador com esse cod {busca}')
    else:
        print(f' -- LEVANTAMENTO DE JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f"   No jogo {i+1} fez {g} gols.")
    print('-'*30)
print("<<<<< PROGRAMA ENCERRADO VOLTE SEMPRE!")