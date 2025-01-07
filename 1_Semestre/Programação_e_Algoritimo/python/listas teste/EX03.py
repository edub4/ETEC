num = []
for cont in range(15):
    num.append(int(input(f'digite o {cont + 1}º valor: ')))

i=1
for numero in num:
    if numero % 2 == 0:
        print(f'{i}º - par')
    else:
        print(f'{i}º - impar')
    i += 1