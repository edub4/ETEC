continuar = 1

while continuar <= 5:
    carC = input('digite um caractar: ')
    numA = float(input('digite um numero: '))
    numB = float(input('digite outro numero: '))

    if carC == '-':
        resultado = numA - numB
        print(resultado)
    elif carC == '+':
        resultado = numA + numB
        print(resultado)
    elif carC == '*':
        resultado = numA * numB
        print(resultado)
    elif carC == '/':
        resultado = numA / numB
        print(resultado)
    else:
        print('não é um operador aritmético valido')


    continuar = continuar + 1