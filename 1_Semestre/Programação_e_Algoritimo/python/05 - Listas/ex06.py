vetorA = []
vetorB = []
qteA = 0
qteB = 0
medA = 0
medB = 0
medTudo = 0

for cont in range (10):
    a = int(input('digite um valor inteiro: '))
    if a % 2 == 0:
        vetorA.append(a)
        qteA += 1
        medA += a
    else:
        vetorB.append(a)
        qteB += 1
        medB += a

medTudo = medA + medB
mediaTudo = medTudo / 10
mediaA = medA / qteA
mediaB = medB / qteB

print(f''' 
   a) - A quantidade de números pares.
   {qteA}
   b) - Os números pares.
   {vetorA}
   c) - A quantidade de números ímpares.
   {qteB}
   d) - Os valores ímpares.
   {vetorB}
   e) - A média dos valores pares.
   {mediaA}
   f) - A média dos valores ímpares.
   {mediaB}
   g) - A média da soma dos valores pares mais os valores ímpares.
   {mediaTudo}
''')
