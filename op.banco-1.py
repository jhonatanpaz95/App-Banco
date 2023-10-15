
menu = '''

[1] depositar
[2] sacar
[3] extrato
[4] sair

=> '''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITES_SAQUES = 3


while True:

    opcao = input(str(f'Escolha a opção desejada {menu}'))

    if opcao == '1':

        print('qual é o valor que deseja depositar')
        valor_deposito = float((input('R$: ')))
        valor_minimo_deposito = 5

        if valor_deposito < valor_minimo_deposito:
            print("Operação Invalida, não é permitido depositos abaixo de R$ 5,00 ")

        saldo += valor_deposito
        extrato.append(str(f'Deposito R$ {valor_deposito}'))

        print(f'o saldo é: R$ {saldo} \n')
        print('Deseja fazer outra operação?')
        
      

    elif opcao == '2':
        print('saque')

        valor_saque = float(input('digite o valor de saque: R$ '))

        if  limite < valor_saque:
            print('Operação invalida, não é permitido saque acima de R$ 500,00')
        elif saldo < valor_saque:
            print('saldo insuficiente')
            print(f'O valor disponivel é R$ {saldo}')

        elif numero_saques < LIMITES_SAQUES:
            saldo -= valor_saque
            numero_saques += 1
            #print(numero_saques)
            extrato.append(str(f'Saque R$ {valor_saque}'))
            print(saldo)
        else:
            print('O numero de saque excede o valor de saques permitidos') #mudar pra uma condição elif pra colocar outro comando no else

        print('Deseja fazer outra operação?')            
       

    elif opcao == '3':
        print('exibir extrato')

        for item in extrato:
            print(item)
            
        print(f'Saldo disponível {saldo}')


    elif opcao == '4':
        break

    else:
        print('operação invalida, por favor selecione novamente a opção desejada.')
