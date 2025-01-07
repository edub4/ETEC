vetor = []

for cont in range(0, 15, 1):
    vetor.append(int(input('digite uma valor: ')))

continuar = True
indice = 0
while continuar:
    achar = int(input('digite o valor para procurar: '))
    for i in range(0, 15):
        if vetor[i] == achar:
            indice = i
        else:
            indice = 'nao cadastrado'

    print(f'seu indice é: {indice}')





    sair = input('digite S para sair ou qualquer tecla para continuar: ')
    if sair.upper() == 'S':
        continuar = False