salario = float(input('digite seu salario: '))

if salario <=600:
    salarionovo = 30/100 * salario + salario
    print(salarionovo)
elif salario <= 1100:
    salarionovo = 25/100 * salario + salario
    print(salarionovo)
elif salario <= 2400:
    salarionovo = 20/100 * salario + salario
    print(salarionovo)
elif salario <= 3550:
    salarionovo = 15/100 * salario + salario
else:
    salario = 10/100 * salario + salario
    print(salario)
