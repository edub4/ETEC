continuar = True
contadorpessoa = 0
contadorpessoainapita = 0

while continuar == True:
    nome = input('digite seu nome: ')
    sexo = input('qual seu sexo [m/f]: ')
    idade = int(input('qual a sua idade: '))
    saude = input('você esta bem de saude[s/n]: ')

    if idade >= 18:
        if saude.lower() == 's':
            if sexo.upper()== 'M':
                print(f'o cidadao {nome} está ato a cumprir o serviço obrigatorio')
                contadorpessoa = contadorpessoa + 1
            else:
                print('você nâo está apto a cumprir o serviço obrigatorio')
                contadorpessoainapita = contadorpessoainapita + 1
        else:
            print('você não está apto a cumprir o serviço obrigatorio')
            contadorpessoainapita = contadorpessoainapita + 1
    else:
        print('você não está apto a cumprir o serviço obrigatorio')
        contadorpessoainapita = contadorpessoainapita + 1

    resposta = input('digite [S] para sair ou qualquer tecla para continuar: ')
    if resposta.upper() == 'S':
        continuar = False

print(f'o numero de pessoas aptas é {contadorpessoa}')
print(f'pessoas inapitas {contadorpessoainapita}')
