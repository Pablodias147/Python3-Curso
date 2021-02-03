boletim = list()
while True:
   nome = str(input("Nome do aluno: "))
   nota1 = float(input("Primeira nota:"))
   nota2 = float(input("segunda nota:"))
   media = (nota1 + nota2) / 2
   boletim.append([nome, [nota1, nota2], media])
   continuar = " "
   while continuar not in "SN":
       continuar = str(input("Dejesa continuar:[S/N] ")).strip().upper()
   if continuar == "N":
       break
print(boletim)
print("=-"*30)
print(f"{'NO.':<4}{'NOME':<10}{'MEDIA':>8}")
print("=-"*30)
for i, a in enumerate(boletim):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    print("-"*25)
    opc = int(input("Mostrar notas de qual aluno?(999 intenrrompe) "))
    if opc == 999:
        break
    if opc <= len(boletim) - 1:
        print(f"Notas de {boletim[opc][0]} São {boletim[opc][1]}")

