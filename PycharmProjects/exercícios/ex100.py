from random import randint, randrange
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores de lista: ", end='')
    sleep(1)
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print("PRONTO!")


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    sleep(0.5)
    print(f'Somando os valores pares de {lista}, temos {soma}')


#PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somaPar(numeros)
