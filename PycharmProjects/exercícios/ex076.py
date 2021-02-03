listagem = ("lápis", 1.10, 'borracha', 0.50, 'caderno', 15, 'mochila', 150, 'caneta', 1)
print("-="* 15)
print('{}'.format("LOJÃO DO PABLO"))
print("-="* 15)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f'R${listagem[pos]:< 7.2f}')
#print(listagem[0], 'R$', listagem[1])