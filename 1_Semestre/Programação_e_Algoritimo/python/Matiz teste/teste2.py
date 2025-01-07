matriz = []

for linha in range(0,3):
    lista = []
    for coluna in range(0,5):
        lista.append(int(input(f'digite o elemento da matiz [{linha},{coluna}]: ')))
    matriz.append(lista)

for linha in range(0,3):
    for coluna in range(0,5,1):
        print(matriz [linha] [coluna], end=' ')
    print()