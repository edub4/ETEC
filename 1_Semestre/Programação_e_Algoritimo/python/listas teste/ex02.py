lista = []
for indice in range (1,11,1):
    nomes = input(f'digite o {indice}ª nome: ')
    lista.append(nomes)

cont = 1
for nome in lista:
    print(f'{cont}ª {nome}')
    cont = cont + 1