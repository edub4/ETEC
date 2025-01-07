pao = float(input('quantos pães você vendeu hoje? '))
broa = float(input('quantas broas você vendeu hoje? '))

valordia = pao * 0.81 + broa * 4.51
poupanca = 0.10 * valordia
aproximado = poupanca * 30

print(f'''
o valor total arrecado foi de R${valordia} 
poupança recebe R${poupanca}
no final do mês sua poupança ficara com o valor aproximado de R${aproximado}  
''')