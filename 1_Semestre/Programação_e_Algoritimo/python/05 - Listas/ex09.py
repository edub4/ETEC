vetorA = []
vetorB = []
vetorC = []

for cont in range(0, 10, 1):
    vetorA.append(int(input('digite um valor numerico: ')))
print()
for cont in range(1, 11, 1):
    vetorB.append(int(input('digite outro valor: ')))

for i in range(0 ,10):
    c = vetorA[i] + vetorB[i]
    vetorC.append(c)
print(f'vetor a: {vetorA}')
print(f'vetor b: {vetorB}')
print(f'vetor c: {vetorC}')