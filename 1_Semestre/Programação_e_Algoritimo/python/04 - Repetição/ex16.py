continuar = 1

while continuar <= 30:
    horas = int(input('digite quantas horas você usou: '))
    tipoCli = input('''digite o numero do seu tipo de residencia.
    (1) Residência	
    (2) Comércio	
    (3) Indústria
    Resposta: ''')

    if tipoCli == '1':
        conta = 0.6 * horas
        print(f'conta:{conta}')
    elif tipoCli == '2':
        conta = 0.48 * horas
        print(f'conta:{conta}')
    elif tipoCli == '3':
        conta = 1.29 * horas
        print(f'conta:{conta}')
    else:
        print('informações invalidas')
