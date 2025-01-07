continuar = 0
mult = 0

while continuar < 10:
    valor = int(input('digite um valor: '))
    mult5 = valor % 5
    if mult5 == 0:
        mult += 1

    continuar += 1

print(f'tem {mult} multiplos de cinco')