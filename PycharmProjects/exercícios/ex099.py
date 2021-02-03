from time import sleep


def maior(*n):
    cont = maior = 0
    print(" ¯\_(ツ)_/¯" * 4)
    print('ANALISANDO OD DADOS PASSADOS...')
    for valor in n:
        print(f'{valor} ', end="", flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

#PROGRAMA PRINCIPAL

maior(2, 9, 4, 5, 7, 1)
maior(0, 4, 0)
maior(1, 2)
maior(6)
maior(0)

#PROGRAMA ALTERNATIVO!!!!!

#if n == 0:
#Def maior(*n):
#    print('ANALISANDO OS DADOS...')
#    print(f'{0} Foram informado {0}')
#    print(f'O maior valor informado foi {0}')
#    print(" ¯\_(ツ)_/¯" * 4)
#print('ANALISANDO OS DADOS...')
#print(f'{n} Foram informado {len(n)}')
#print(f'O maior valor informado foi {max(n)}')
#print(" ¯\_(ツ)_/¯" * 4)