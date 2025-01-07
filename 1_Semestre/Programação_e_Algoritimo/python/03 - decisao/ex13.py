venda = float(input('digite o valor da venda: '))
print('agora escolha a forma de pagamento digitando o numero dela:')

pagamento = int(input('''(1) - Venda a Vista - desconto de 10%' /n
(2) - Venda a Prazo 30 dias - desconto de 5%
(3) - Venda a Prazo 60 dias - mesmo preço
(4) - Venda a Prazo 90 dias - acréscimo de 5%
(5) - Venda com cartão de débito - desconto de 8%
(6) - Venda com cartão de crédito - desconto de 7% 
Escolha :  '''))

match pagamento:
    case 1:
        final = venda - 0.05 * venda
        print(f'O produto de {venda} ficara {final} com essa forma de pagamneto')
    case 2:
        final = venda - 0.05 * venda
        print(f'O produto de {venda} ficara {final} com essa forma de pagamneto')
    case 3:
        print('o produto ficara com mesmo preço pois a forma de pagamento escolhida não tem desconto')
    case 4:
        final = venda + 0.05 * venda
        print(f'O produto de {venda} ficara {final} com essa forma de pagamneto')
    case 5:
        final = venda - 0.08 * venda
        print(f'O produto de {venda} ficara {final} com essa forma de pagamneto')
    case 6:
        final = venda - 0.07 * venda
        print(f'O produto de {venda} ficara {final} com essa forma de pagamneto')
    case _:
        print('a opção escolhida não tem')
