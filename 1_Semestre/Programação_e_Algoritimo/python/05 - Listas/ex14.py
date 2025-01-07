nome = []
nota = []
contAlunosCad = 0

continuar = True
while continuar:
    nome.append(input('digite o nome do aluno: '))
    nota.append(float(input('digite a nota do aluno: ')))
    contAlunosCad += 1

    saida = input('N para sair: ')
    if saida.upper() == 'N':
        continuar = False

aluno = input('qual aluno deseja procurar: ')

for x in nome:
    for y in nota:
        if x == aluno:
            print(f'aluno: {x}   nota: {y}')
            break
