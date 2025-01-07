n1 = int(input('digite um numero: '))
n2 = int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1 > n2:
    if n1 > n3:
        maior = n1
        print(f'o maior  numero é {maior}')

if n2 > n1:
    if n2 > n3:
        maior = n2
        print(f'o maior numero é {maior}')

if n3 > n1:
    if n3 > n2:
        maior = n3
        print(f'o maior numero é {maior}')