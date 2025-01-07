nome = input('digite seu nome: ')
salario = float(input('digite seu salario atual: '))
cargo = input('digite seu cargo (diretor, gerente ou lider): ')
local = input('digite seu local de trabalho (interno ou externo): ')

if local == 'externo':
    premio = 0.20 * salario + salario
else:
    if local == 'interno':
        premio = 0.10 * salario + salario


if cargo == 'diretor':
    salfim = 1000 + premio
else:
    if cargo == 'gerente':
        salfim = 500 + premio
    else:
        if cargo == 'lider':
            salfim = 200 + premio

print(f'''
O funcionario {nome} com o cargo de {cargo} 
trabalhando no {local} do estabelecimento recebe o
novo salario de R${salfim}''')