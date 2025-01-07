continuar = True
par = 0
impar = 0

numinicial = int(input('digite um valor inicial: '))
numfinal = int(input('digite um valor final: '))

for imparpar in range( numinicial ,numfinal):
     print(imparpar)

     resultado = imparpar % 2

     if resultado == 0:
         par = par + 1
     else:
         impar = impar + 1

print(f'par:{par}  impar:{impar}')