r1 = float(input("primeiro segimento:"))
r2 = float(input("segundo segimento:"))
r3 = float(input("terceiro segimento:"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triangulo", end="")
    if r1 == r2 == r3:
        print("equilaterro")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else: print("ISOSCELES")

else: print("Nao pode formar um triangulo")