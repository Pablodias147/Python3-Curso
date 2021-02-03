nome = str(input('qual é seu nome?'))
nome.title()
if nome == 'Pablo':
    print('Que nome lindo voce tem!')
elif nome == "Gabriel" or nome == "Pedro" or nome == "Maria":
    print("Seu nome é conhecido no Brasil")
elif nome in "Gustavo Joao Claudinho":
    print("que nome em amigo")
else:
    print('seu nome é tao normal')
print('bom dia {}'.format(nome))
