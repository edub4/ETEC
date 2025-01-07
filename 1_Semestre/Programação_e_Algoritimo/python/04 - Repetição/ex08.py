continuar = 0

while continuar < 10:
    nome = input('digite o nome do funcionario: ')
    idade = int(input('digite sua idade: '))
    sexo = input('qual seu sexo "M" ou "F": ')

    if sexo.upper() == 'M':
        if idade >= 30:
            print(f'{nome} recebera um salário líquido de R$100')
        else:
            print(f'{nome} recebera um salário líquido de R$50')
    elif sexo.upper() == 'F':
        if idade >= 30:
            print(f'{nome} recebera um salário líquido de R$200')
        else:
            print(f'{nome} recebera um salário líquido de R$80')

    continuar = continuar + 1