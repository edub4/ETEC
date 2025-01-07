n1 = int(input('digite um numero inteiro: '))
n2 = int(input('digite um numero inteiro: '))
n3 = int(input('digite um numero inteiro: '))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            fim = n1 + n2
            print (fim)
        else:
            fim = n1 + n3
            print (fim)
    else:
        fim = n1 + n3
        print (fim)
else:
    if n1 > n3:
        fim = n1 + n2
        print (fim)
    else:
        fim = n2 + n3
        print (fim)