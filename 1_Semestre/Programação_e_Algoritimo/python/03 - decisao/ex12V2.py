nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

if idade >= 5 and idade <= 10:
    categoria = ('infantil')
    print(f'o jogador {nome} esta na categoria {categoria}')
elif idade <= 15:
    categoria = ('juvenil')
    print(f'o jogador {nome} esta na categoria {categoria}')
elif idade <= 20:
    categoria = ('junior')
    print(f'o jogador {nome} esta na categoria {categoria}')
elif idade <= 25:
    categoria = ('profissional')
    print(f'o jogador {nome} esta na categoria {categoria}')
else:
    print('esse jogador não está na faxa etaria')