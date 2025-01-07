listaA = []
listaB = []
listaC = []

for cont in range(0,10):
    listaA.append(int(input('digite um valor: ')))

print()
for cont in range(0,10):
    listaB.append(int(input('digite outro valor valor: ')))

i = 0
while i < 10:
    listaC.append(listaA[i] + listaB[i])
    i += 1

print(f'vetor A: {listaA}')
print(f'vetor B: {listaB}')
print(f'vetor C: {listaC}')