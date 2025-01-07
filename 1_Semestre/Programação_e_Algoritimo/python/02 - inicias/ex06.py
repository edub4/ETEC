nome = input("digite seu nome: ")
salario = float(input('digite seu salario: '))
vendas = float(input("digite quantas vendas você fez em dinheiro"))

salfim = salario + ( 15/100 * vendas )

print(f"o vendedor {nome} tem o salario inicial de {salario} mas com a comissão o seu salario final fica {salfim}")