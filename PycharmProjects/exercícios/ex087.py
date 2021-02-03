matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f"Digite um valor para {l} {c}: "))
print("+="* 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[l][c]:^5}]", end="")
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print("+="* 20)
print(f"As somas dos valores pares foram {spar}")
for l in range(0, 3):
    scol += matrix[l][2]
print(f"A soma da terceira coluna foi {scol}")
for c in range(0, 3):
    if c == 0:
        mai = matrix[1][c]
    elif matrix[1][c] > mai:
        mai = matrix[1][c]
print(f"O maior elemento da segunda linha é {mai }")