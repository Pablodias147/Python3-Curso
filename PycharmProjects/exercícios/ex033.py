n1 = float(input("fala um numero:"))
n2 = float(input("fala um segundo numero:"))
n3 = float(input("fala um terceiro numero:"))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior =  n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print("o maior numero é {}\nO menor numero é {}".format(maior, menor))