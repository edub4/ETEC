nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))

if idade >= 5:
    if idade <= 10:
        categoria = ('infantil')
        print(f'o jogador {nome} esta na categoria {categoria}')
if idade >= 11:
    if idade <= 15:
        categoria = ('juvenil')
        print(f'o jogador {nome} esta na categoria {categoria}')
if idade >= 16:
    if idade<= 20:
        categoria = ('junior')
        print(f'o jogador {nome} esta na categoria {categoria}')
if idade >= 21:
    if idade <= 25:
        categoria = ('profissional')
        print(f'o jogador {nome} esta na categoria{categoria}')
if idade < 5:
    if idade > 25:
        print('esse jogador não esta na faixa etaria ')