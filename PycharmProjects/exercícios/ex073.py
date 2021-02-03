tabela = ('Atlético - MG', 'São Paulo', 'Flamengo', 'Internacional',
          'Palmeiras', 'Santos','Grêmio', 'Fluminense', 'Fortaleza',
          'Ceará', 'Corinthians', 'Athletico - PR', 'Bahia','Atlético - GO ',
          'Bragantino', 'Sport', 'Vasco', 'Coritiba','Botafogo', 'Goiás ')
print("-="* 50)
print(f"A lista dos times do brasilheirão são{tabela}")
print("-="* 50)
print(f'Os primeiros 5 times são {tabela[:5]}')
print("-="* 50)
print(f'Os ultimos 4 são {tabela[-4:]}')
print("-="* 50)
print(f"Times em ordem alfabetica {sorted(tabela)}")
print("-="* 50)
print("O Santos esta na {}ª posição".format(tabela.index("Santos")+ 1))