contador = 1
reajuste = 0
conta = 0

while contador <= 584:
    nome = str(input(f'digite o nome do {contador}ª funcionario: '))
    salFuncionario = float(input('digite o salario do funcionario:'))
    salMinimo = float(input('digite o valor do salrio minimo atual: '))

    if salFuncionario < salMinimo * 3:
       salNovo = (salFuncionario * 0.5) + salFuncionario
       print(f'O(a) funcionario(a) {nome} teve o reajuste de 50% igual a R${conta}. R${salNovo}')
       reajuste = (salFuncionario * 0.5) + reajuste
       conta = salFuncionario * 0.5

    elif salFuncionario >= salMinimo * 3 and salFuncionario < salMinimo * 10:
        salNovo = (salFuncionario * 0.2) + salFuncionario
        print(f'O(a) funcionario(a) {nome} teve o reajuste de 20% igual a R${conta}. R${salNovo}')
        reajuste = (salFuncionario * 0.2) + reajuste
        conta = salFuncionario * 0.2

    elif salFuncionario >= salMinimo * 10 and salFuncionario < salMinimo * 20:
        salNovo = (salFuncionario * 0.15) + salFuncionario
        print(f'O(a) funcionario(a) {nome} teve o reajuste de 15% igaul a R${conta}. R${salNovo}')
        reajuste = (salFuncionario * 0.15) + reajuste
        conta = salFuncionario * 0.15

    else:
        salNovo = (salFuncionario * 0.1) + salFuncionario
        print(f'O(a) funcionario(a) {nome} teve o reajuste de 10% igual a R${conta}. R${salNovo}')
        reajuste = (salFuncionario * 0.1) + reajuste
        conta = salFuncionario * 0.1

    contador = contador + 1

print(f'a folha de pagamento aumentou R${reajuste}')