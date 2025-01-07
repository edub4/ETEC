continuar = 1

while continuar <= 50:
    nivelP = int(input('digite seu nivel [1,2,3]: '))
    horaP = float(input('digite quantas horas você fez: '))

    if nivelP == 1:
        salario = 12 * horaP
        print(salario)
    elif nivelP == 2:
        salario = 17 * horaP
        print(salario)
    elif nivelP == 3:
        salario = 25 * horaP
        print(salario)
    else:
        print('informações invalidas')

    continuar = continuar + 1
