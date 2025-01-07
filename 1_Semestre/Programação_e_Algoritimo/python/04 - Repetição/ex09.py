continuar = True

while continuar:
    nome = input('digite seu nome: ')
    idade = int(input('digite sua idade: '))
    risco = input('qual seu nivel de risco [baixo/medio/alto]: ')

    if idade >= 17 and idade <= 20:
        if risco.lower() == 'baixo':
            print(f'o(a) cliente {nome} recebera uma categoria de 1')
        elif risco.lower() == 'medio':
            print(f'o(a) cliente {nome} recebera uma categoria de 2')
        elif risco.lower() == 'alto':
            print(f'o(a) cliente {nome} recebera uma categoria de 3')
        else:
            print('informações informadas são invalidas')
    elif idade >= 21 and idade <= 24:
        if risco.lower() == 'baixo':
            print(f'o(a) cliente {nome} recebera uma categoria de 2')
        elif risco.lower() == 'medio':
            print(f'o(a) cliente {nome} recebera uma categoria de 3')
        elif risco.lower() == 'alto':
            print(f'o(a) cliente {nome} recebera uma categoria de 4')
        else:
            print('informações informadas são invalidas')
    elif idade >= 25 and idade <= 34:
        if risco.lower() == 'baixo':
            print(f'o(a) cliente {nome} recebera uma categoria de 3')
        elif risco.lower() == 'medio':
            print(f'o(a) cliente {nome} recebera uma categoria de 4')
        elif risco.lower() == 'alto':
            print(f'o(a) cliente {nome} recebera uma categoria de 5')
        else:
            print('informações informadas são invalidas')
    elif idade >= 35 and idade <= 64:
        if risco.lower() == 'baixo':
            print(f'o(a) cliente {nome} recebera uma categoria de 4')
        elif risco.lower() == 'medio':
            print(f'o(a) cliente {nome} recebera uma categoria de 5')
        elif risco.lower() == 'alto':
            print(f'o(a) cliente {nome} recebera uma categoria de 6')
        else:
            print('informações informadas são invalidas')
    elif idade >= 65 and idade <= 70:
        if risco.lower() == 'baixo':
            print(f'o(a) cliente {nome} recebera uma categoria de 7')
        elif risco.lower() == 'medio':
            print(f'o(a) cliente {nome} recebera uma categoria de 8')
        elif risco.lower() == 'alto':
            print(f'o(a) cliente {nome} recebera uma categoria de 9')
        else:
            print('informações informadas são invalidas')
    else:
        print(f'o(a) cliente {nome} não está na faixa etaria nescessaria. Anos:{idade}')
    print()


    sair = input('deseja continuar "S" ou "N": ')
    if sair.upper() == 'N':
        continuar = False