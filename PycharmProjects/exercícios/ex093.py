dados = dict()
aproveitamento = list()
dados["nome"] = str(input("Nome: "))
dados["partidas"] = int(input("Quantas partidas? "))
for c in range(dados["partidas"]):
    gols = (int(input(f"Quantos gols no {c + 1}º jogo: ")))
    aproveitamento.append(gols)
dados["total"] = sum(aproveitamento)
dados["gols"] = aproveitamento.copy()
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas")
for c, v in enumerate(aproveitamento):
    print(f"Na {c + 1}º partida. Fez {v} gols.")

print(f"Um total de {dados['total']} gols")
