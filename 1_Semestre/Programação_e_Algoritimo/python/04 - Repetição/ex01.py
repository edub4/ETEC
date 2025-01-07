contador = 1
qtnumero = 0

while contador <= 80:
    numeros = int(input(f'digite o {contador}ª numero: '))
    if numeros >= 10 and numeros <=150:
        qtnumero = qtnumero + 1
    contador = contador + 1
print(f'foram encontrados {qtnumero} numero(s) entre 10 e 150')