vet = []
par = []
impar = []
contimpar = 0
contpar = 0
medpar = 0
medimpar = 0

for cont in range (0,10):
    vet.append(int(input('insira um numero inteiro: ')))

cont = 0
while cont > 11:
    for v in vet:
        if v % 2 == 0:
            contpar += 1
            par.append(v)
            medpar += v
        else:
            contimpar += 1
            impar.append(v)
            medpar += v

mediaP = medpar / contpar
mediaIm = medimpar/contimpar
mediaTudo = (medimpar + medimpar)/cont

print(f'''
   a) - A quantidade de números pares.
      R: {contpar}
   b) - Os números pares.
      R: {list(par)}
   c) - A quantidade de números ímpares.
      R: {contimpar}
   d) - Os valores ímpares.
      R: {list(impar)}
   e) - A média dos valores pares.
      R: {mediaP}
   f) - A média dos valores ímpares.
      R: {mediaIm}
   g) - A média da soma dos valores pares mais os valores ímpares.
      R: {mediaTudo}
''')
     

