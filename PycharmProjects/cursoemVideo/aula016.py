lanche = ("Hamburgue", 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos ,comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")

for cont in range(0, len(lanche)):
    print(f"Vou comer {lanche[cont]} na posição {cont}")
