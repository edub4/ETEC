continuar = 0
mediaVenda = 0
mediaCusto = 0

while continuar < 40:
    precoCusto = float(input(f'qual o preço de custo do produto: '))
    precoVenda = float(input(f'qual o preço de venda do produto: '))

    if precoVenda > precoCusto:
        print('esse produto teve lucro')
    elif precoVenda < precoCusto:
        print('esse produto teve prejuízo')
    else:
        print('esse produto deu empate')
    print()

    mediaVenda = precoVenda + mediaVenda
    mediaCusto = precoCusto + mediaCusto

    continuar = continuar + 1

mediaV = mediaVenda / continuar
mediaC = mediaCusto / continuar

print()
print(f'média de venda {mediaV}')
print(f'média de custo {mediaC}')