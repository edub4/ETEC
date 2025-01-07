a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))

if a > b:
    if a > c:
        if c > b:
            resultado = c + a
            print(f'resultado {resultado}')
        else:
            resultado = a + b
            print(f'resultado {resultado}')

if b > a:
    if b > c:
        if a > c:
            resultado = b + a
            print(f'resultado {resultado}')
        else:
            resultado = c + b
            print(f'resultado {resultado}')

if c > a:
    if c > b:
        if a > b:
            resultado = c + a
            print(f'resultado {resultado}')
        else:
            resultado = c + b
            print(f'resultado {resultado}')