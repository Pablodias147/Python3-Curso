print("-"* 20)
print("Sequencia de Fibonacci")
print("-"* 20)
n = int(input("Quantos termos voce quer mostrar:"))
t1 = 0
t2 = 1
cont = 3
print("{} - {}".format(t1, t2), end="")
while cont <= n:
    t3 = t1 + t2
    print(" - {}".format(t3), end="")
    cont += 1
    t1 = t2
    t2 = t3
print("\nFIM")
