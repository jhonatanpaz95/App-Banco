
menu = '''

[1] depositar
[2] sacar
[3] extrato
[4] sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITES_SAQUES = 3


while True:

    opcao = input(str(f'Escolha a opção desejada {menu}'))

    if opcao == '1':

        print('qual é o valor que deseja depositar')
        valor_deposito = float((input('R$: ')))
        valor_minimo_deposito = 5

        if valor_deposito < valor_minimo_deposito:
            print("Operação Invalida")

        saldo += valor_deposito

        print(f'o saldo é: R$ {saldo} \n')
        print('Deseja fazer outra operação?')
        
      

    elif opcao == '2':
        print('saque')

    elif opcao == '3':
        print('exibir extrato')

    elif opcao == '4':
        break

    else:
        print('operação invalida, por favor selecione novamente a opção desejada.')
