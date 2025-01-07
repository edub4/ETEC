continuar = 0

while continuar <5:
    l1 = int (input('digite um valor: '))
    l2 = int (input('digite outro valor: '))
    l3 = int (input('digite outro valor: '))
    print()

    if l1 > 0:
        print('o lado 1 pode ser o lado de um triangulo')
    else:
        ('o lado 1 não pode ser o lado de um triangulo')
    if l2 > 0:
        print('o lado 2 pode ser o lado de um triangulo')
    else:
        ('o lado 2 não pode ser o lado de um triangulo')
    if l3 > 0:
        print('o lado 3 pode ser o lado de um triangulo')
    else:
        print ('o lado 3 não pode ser o lado de um triangulo')

    if l1 == l2:
        if l2 == l3:
            print('é um triangulo equilatero e isoceles')
        else:
            print('é um triangulo isoceles')
    elif l2 == l3:
        print('é um triangulo isoceles')
    else:
        print('é um triangulo escaleno')
    print ()