somaidade = 0
mediaidade= 0
maioridadehomem = 0
nomevelho = ""
menosde20anos = 0
nomemulher = ""
for p in range(1, 5):
    nome = str(input("Qual o nome da {} pessoa:".format(p)))
    idade = int(input("Qual a idade da {} pessoa:".format(p)))
    sexo =  str(input("Qual o sexo da {} pessoa:[M/F]".format(p)))
    somaidade += idade
    if p == 1 and sexo in "Mn":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mn" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        menosde20anos = 1
        nomemulher += " ",  nome
mediaidade = somaidade / 4
print("A media de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} e se chama {}".format(maioridadehomem, nomevelho))
print("Existe {} com menos de vinte anos. e o nome delas são {}".format(menosde20anos, nomemulher))
