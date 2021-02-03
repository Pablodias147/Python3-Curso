
while True:
    num = int(input("Voce quer ver qual tabuada?"))
    if num < 0:
        break
    for res in range(1, 11):
        tab = num * res
        print(f"{num} x {res} = {tab}")
print("Programa encerrado! Volte sempre.")