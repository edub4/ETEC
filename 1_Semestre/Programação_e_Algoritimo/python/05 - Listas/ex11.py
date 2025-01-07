lista = []
a = 0
b = 0
maior = 0
for cont in range(0, 10, 1):
    lista.append(int(input('digite um valor: ')))

a = 0
b = 1
for cont in range(0, 5):
    n1 = lista[a]
    a += 1
    n2 = lista[a]
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    a += 1

for cont in range(0, 5, 1):
    for num in lista:
        if maior < num:
            maior = num


print(f'o menor numero è: {maior}')
print(f'a lista: {lista}')