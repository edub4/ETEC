continuar = True

while continuar == True:

    numero = int(input('informe o valor: '))
    if numero > 80:
        print(f'o numero {numero} é maior que 80')
    elif numero < 25:
        print(f'o numero {numero} é menor que 25')
    elif numero == 40:
        print(f'o numero {numero} é igual a 40')


    saida = input('Aperte S, para continuar aperte qualquer tecla')
    if saida.upper() == 'S':
        continuar = False