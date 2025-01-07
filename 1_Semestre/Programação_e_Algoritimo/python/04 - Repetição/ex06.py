continuar = True
carrosDoisMil = 0
carrosGeral = 0

while continuar:
    carro = input('qual o nome do carro: ')
    anoCarro = int(input('qual o ano do carro: '))
    precoCarro = float(input('qual o preço atual do carro: '))

    if anoCarro <= 2000:
        precoNovo = precoCarro - (precoCarro * 0.12)
        carrosDoisMil = carrosDoisMil + 1
        print(f'o carro {carro} esta avaliado em R${precoNovo}')
    else:
        precoNovo = precoCarro - (precoCarro * 0.07)
        print(f'o carro {carro} esta avaliado em R${precoNovo}')

    carrosGeral = carrosGeral + 1

    if input('deseja continar "S" ou "N": ').upper() == 'N':
        continuar = False
print()
print(f'o total de carros até os anos 2000 é {carrosDoisMil}')
print(f'o total de carros foram de {carrosGeral}')