from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} ate {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print()
        print("FIM!")
        sleep(1)
    else:
        cont = i
        while cont >= f:
            print(f' {cont} ', end="", flush=True)
            sleep(0.5)
            cont -= p
        print()
        print("FIM!")
        sleep(1)


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print()
print("Agora é sua vez de personalizar o programa!")
ini = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(ini, fim, passo)
