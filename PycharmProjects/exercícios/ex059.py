from time import sleep
sair = False
valor1 = float(input("Digite um valor:"))
valor2 = float(input("Digite um valor:"))
while not sair:
    sleep(0.3)
    print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos numeros\n[5] Sair")
    escolha = int(input("O quer voce vai fazer:"))
    sleep(0.5)
    if escolha == 1:
        soma = valor1 + valor2
        print("A soma dos dois valores foi {}".format(soma))
    if escolha == 2:
        mult = valor1 * valor2
        print("A multiplicação dos dois numeros foi {}".format(mult))
    if escolha == 3:
        if valor1 > valor2:
            print("{} é maior que {}".format(valor1, valor2))
        elif valor2 > valor1:
            print("{} é maior que {}".format(valor2, valor1))
        else: print("Os valores sao os mesmo.")
    if escolha == 4:
        valor1 = float(input("Digite um valor:"))
        valor2 = float(input("Digite um valor:"))
    if escolha == 5:
        sair = True
