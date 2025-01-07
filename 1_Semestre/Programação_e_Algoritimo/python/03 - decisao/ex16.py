a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))

if a > b:
    if a > c:
        if b > c:
            print(f'{c}{b}{a}')
        else:
            print(f"{b}{c}{a}")
if b > a:
    if b > c:
        if a > c:
            print(f'{c}{a}{b}')
        else:
            print(f'{a}{c}{b}')
if c > a:
    if c > b:
        if a > b:
            print(f'{b}{a}{c}')
        else:
            print(f'{a}{b}{c}')