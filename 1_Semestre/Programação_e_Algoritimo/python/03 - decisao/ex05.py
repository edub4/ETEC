salario = float(input('digite seu salario: '))

if salario <= 600:
    salario1 = 30/100 * salario + salario
    print(f'30% {salario1}')
else:
    if salario >= 600.01:
        if salario <= 1100:
            salario2 = 25/100 * salario + salario
            print (f'25% {salario2}')
        else:
            if salario >= 1100.01:
                if salario <= 2400:
                    salario3 = 20/100 * salario + salario
                    print (f'20% {salario3}')
                else:
                    if salario >= 2400.01:
                        if salario <= 3550:
                            salario4 = 15/100 * salario + salario
                            print (f'15% {salario4}')
                        else:
                            if salario > 3550:
                                salario5 = 10/100 * salario + salario
                                print (f'10% {salario5}')
