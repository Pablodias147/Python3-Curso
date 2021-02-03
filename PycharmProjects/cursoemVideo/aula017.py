num= [10,5, 6, 3, 1, 7, 1]
num[3] = 10
num.append(11)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print("Nao achei o numero 4")
print(num)
print(f'Essa lista tem {len(num)} elementos')
