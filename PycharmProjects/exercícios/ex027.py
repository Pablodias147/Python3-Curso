nome = str(input("Qual é seu nome?")).strip()
print("Muito prazer em te conhecer")
n = nome.split()
print("Seu primeiro nome é {}\nSeu ultimo nome é {}".format(n[0], n[len(n)-1]))
