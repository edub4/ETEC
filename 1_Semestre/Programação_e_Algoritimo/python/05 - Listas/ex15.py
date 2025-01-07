vetor = []
vetor2 = []

for cont in range(1,11,1):
    vetor.append(int(input(f'digite o {cont} valor: ')))

for i in range(9,-1,-1):
    vetor2.append(vetor[i])


print(vetor2)
print(vetor)
