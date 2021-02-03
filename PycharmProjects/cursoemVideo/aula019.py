def soma(a, b):
    c = a + b
    print(c)


soma(2, 2)


def contador(* num):
    tamanho = len(num)
    print(f'Recebi os valores {num}. são ao todo {tamanho} numeros.')


contador(1, 5, 6, 7)
contador(3, 1, 2, 8, 4)
contador(1, 2, 3)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)