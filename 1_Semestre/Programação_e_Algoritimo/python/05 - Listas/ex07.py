lista = []
continuar = 0

while continuar < 10:  
    valor = float(input('digite um valor: '))
    if valor in lista:
        print('valor ja cadastrado')
    else:
        lista.append(valor)
    continuar += 1

for n in lista:
    print (n)