sexo = str(input("Informe seu sexo [S/F]:"))[0]
while sexo not in "MmFf":
    sexo = str(input("Dados invalidos, Por favor, Informe se usexo:")).strip().upper()[0]
print("Sexo {} Registrado com secesso".format(sexo))