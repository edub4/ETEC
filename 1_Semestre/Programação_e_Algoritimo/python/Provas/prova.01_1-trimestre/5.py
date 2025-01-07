print('''o valores das camisetas:
grande = 71
media = 63
pequena = 59
''')
grande = float(input('digite quantas camisetas grandes você quer: '))
medio = float(input('digite quantas camisetas medias você quer: '))
pequeno = float(input('digite quantas camisetas pequenas você quer: '))

valorg = grande * 71
valorm = medio * 63
valorp = pequeno * 59
valorfim = valorp + valorm + valorg

print(f'''
o valor final ficou R${valorfim} sendo:
G = R${valorg}
M = R${valorm}
P = R${valorp}''')