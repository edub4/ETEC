cont = 1
qt_numeros_intervalo = 0
while cont <= 8:
    numero = int(input(f' Digite o {cont} numero : '))
    if numero >= 10 and numero <= 150:
        qt_numeros_intervalo = qt_numeros_intervalo + 1
    cont = cont + 1
print(f' Foram Encontrados {qt_numeros_intervalo} numeros entre 10 e 150. ')
