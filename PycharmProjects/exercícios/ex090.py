sala_2A5 = dict()
sala_2A5['aluno'] = str(input("Nome: "))
sala_2A5['media'] = float(input(f"Media de {sala_2A5['aluno']}: "))

if sala_2A5["media"] >= 7:
    sala_2A5["situação"] = "Aprovado"
elif 5<= sala_2A5['media'] <= 7:
    sala_2A5["situação"] = "Recuperação"
else:
    sala_2A5["situação"] = "Reprovado"
for k, v in sala_2A5.items():
    print(f"{k} é igual a {v}")
