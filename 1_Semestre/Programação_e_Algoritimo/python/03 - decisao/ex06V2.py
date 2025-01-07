lanche = int(input('digite o codigo do seu lanche: '))

if lanche == 100:
    print('X-Salada com coca-cola.')
elif lanche == 200:
    print('Hot dog com suco de laranja')
elif lanche == 300:
    print('Sanduiche natural com suco de uva.')
elif lanche == 400:
    print('Misto Quente com fanta laranja.')
elif lanche == 500:
    print('Pão com manteiga com café.')
elif lanche == 600:
    print('Hot dog com suco de laranja')
elif lanche != 100 and lanche != 200 and lanche != 300 and lanche != 400 and lanche != 500 and lanche != 600:
    print('codigo inavlido')