lista = []
lPar = []
lImpar = []

for cont in range(0, 10, 1):
    lista.append(float(input('digite um valor numerico: ')))

for num in lista:
    if num % 2 == 0:
        lPar.append(num)
    else:
        lImpar.append(num)

print(f'lista principal: {lista}')
print(f'lista par: {lPar}')
print(f'lista impar: {lImpar}')
