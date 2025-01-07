#soma, subitrção, divisão e multplivaçao

#entrada de dados
n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))

#processamento
subi = n1 - n2
soma = n1 + n2
multi = n1 * n2
divi = n1 / n2

#saida
print('a soma do numero {} mais o {} é {} ' .format(n1,n2,soma))
print('subitração: ', subi)
print(f'a multiplicação de {n1} * {n2} é {multi}')
print(f'a divisão é {divi}')
