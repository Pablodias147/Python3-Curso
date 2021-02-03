pessoas = {'nome': 'Pablo', 'idade': 17, 'sexo': "M"}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
for k, v in pessoas.items():
    print(f"{k} = {v}")
estado = dict()
brasil = list()
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
for e in brasil:
    for f, g in e.items():
        print(f"O campa {f} tem valor {g}")