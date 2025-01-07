t1 = input('digite o nome do time: ')
t2 = input('digite o nome do outro time: ')

golst1 = int(input(f'digite quantos gols o time {t1} fez: '))
golst2 = int(input(f'digite quantos gols o time {t2} fez: '))

if golst1 > golst2:
    print(f'o vencedor é {t1} com {golst1} gols')
else:
    if golst1 < golst2:
        print(f'o vencedor é {t2} com {golst2} gols')
    if golst1 == golst2:
        print('ficaram empatados')
