n1 = int(input('digite a nota do primeiro semestre: '))
n2 = int(input('digite a nota do segundo semestre: '))
n3 = int(input('digite a nota do terceiro semestre: '))

media =  n1 + n2 + n3 / 3

if media <= 5:
    print (f'nota:{media} situação: reprovado')
if media >= 7:
    print (f'sua nota :{media} situação: aprovado')
else:
    print (f'nota:{media} situação: reperação')