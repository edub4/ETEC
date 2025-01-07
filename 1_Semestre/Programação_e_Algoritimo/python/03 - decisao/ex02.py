n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if n1 < n2:
    print(f'A ordem crescente dos numeros é {n1,n2}')
else:
    n3 = n1
    n1 = n2
    n2 = n3
    print(f'a ordem dos numeros sera {n1,n2}')