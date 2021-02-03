from random import sample
texto = print("Ordem de alunos que vão apresentar o trabalho")
a1 = input('Primeiro aluno:')
a2 = input('Segundo aluno:')
a3 = input('Terceiro aluno:')
a4 = input('Quarto aluno:')
lista = [a1, a2, a3, a4]
ordem = sample(lista, k=4)
print('A ordem de apresentação será {}'.format(ordem))
