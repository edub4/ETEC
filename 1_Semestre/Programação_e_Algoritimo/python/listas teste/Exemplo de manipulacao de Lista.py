numeros = [] # criar uma lista vazia
valores = [10,20,30,40,50] # criar uma lista com elementos
lista_diversa = [1, 2.5, 'Teste', True]
# print(f'{numeros[0]}, {valores[1]}, ')
print(valores)
valores[2] = 300
print(valores[2])
print('O último elemento da lista:', valores[-1])

del(valores[0]) # remove o elemento por índice
print(valores)

valores.pop() # remove o último elemento
valores.pop(1) # remove o elemento de acordo com o índice
print(valores)

valores.remove(40) # remove o elemento pelo seu valor
print(valores)

numeros.append(10)
print(numeros[0])

valores.append(1000)
valores.append(1001)
valores.append(1002)
print(valores)

# iteração pelo índice
i = 0
while i <= 3:
    print(valores[i])
    i = i + 1

for valor in valores:
    print(valor)

# operadores IN NOT IN
resposta = 10010 in valores
print(resposta)

if 1001 in valores:
    print("O valor procurado está na lista")
else:
    print("O valor procurado não está na lista")