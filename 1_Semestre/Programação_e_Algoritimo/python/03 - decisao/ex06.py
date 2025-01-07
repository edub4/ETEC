lanche = int(input('informe o codigo do produto: '))

match lanche:
    case 100:
        input('X-Salada com coca-cola.')
    case 200:
        input('Hot dog com suco de laranja.')
    case 300:
        input('Sanduiche natural com suco de uva.')
    case 400:
        input('Misto Quente com fanta laranja.')
    case 500:
        input('Pão com manteiga com café.')
    case 600:
        input('Pão com manteiga na chapa com café com leite.')
    case _:
        input('codigo invalido')