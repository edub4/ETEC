nome = input(' Digite o seu nome ')
sexo = input(' Digite o seu sexo: M ou F ')
idade = int(input(' Digite a sua idade '))
saude = input(' Digite a situação da sua saúde: B ou R ')

qtd_pessoas_aptas = 0
qtd_pessoas_inaptas = 0
continuar = True
while continuar == True:

    if idade >= 18 and saude.upper() == 'B' and sexo.upper() == 'M':
        print(f' A pessoa {nome} esta Ápta para servir o exército brasileiro. ')
        qtd_pessoas_aptas = qtd_pessoas_aptas + 1
    else:
        print(f' {nome} não esta Ápta para servir o exército brasileiro. ')
        qtd_pessoas_inaptas = qtd_pessoas_inaptas + 1

    resposta = input(' Digite S para sair ou qualquer tecla para continuar: ')
    if resposta.upper() == 'S':
        continuar = False

print(f' Encontrei {qtd_pessoas_aptas} Áptas para o serviço militar brasileiro ')
print(f' Encontrei {qtd_pessoas_inaptas} Ináptas para o serviço militar brasileiro')
