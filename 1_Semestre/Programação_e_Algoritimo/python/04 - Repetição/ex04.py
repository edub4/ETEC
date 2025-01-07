continuar = True

while continuar:

    numero = int(input('digite um numero: '))

    if numero > 0:
        print(f'o {numero} é positivo')
    elif numero < 0:
        print(f'o {numero} é negativo')
    else:
        print(f'o {numero} é Zero')

    if input('digite S para sair, aperte qualquer tecla para continuar').upper() == 'S':
        continuar = False
