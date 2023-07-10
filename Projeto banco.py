menu = """
Seja Bem-Vindo!

Selecione a opção desejada:

[a] - Depositar
[b] - Sacar
[c] - Extrato
[d] - Sair
"""
saldo = 0
limite_saque = 500
limite_saque_diario = 3
saque_diario = 0
extrato = ""

while True:
    opcao = input(menu)
    
    if opcao == 'a':
        valor = float(input('Valor que deseja depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito R${valor:.2f}\n'
        
        else:
            print('Não foi possivel depositar esse valor.')

    elif opcao == 'b':
        valor = float(input('Digite o valor que deseja sacar: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque_diario = saque_diario >= limite_saque_diario

        if excedeu_saldo:
            print('Seu saldo é insuficiente para saque.')

        elif excedeu_limite:
            print('Valor desejado maior que limite de saque')

        elif excedeu_saque_diario:
            print('Saques diários já foram utilizados')

        elif valor > 0:
            saque_diario += 1
            saldo -= valor
            extrato += f'Saque R${valor:.2f}\n'
        else:
            print('Operação falhou, valor informado é inválido.')

    elif opcao == 'c':
        print('\n ========== Extrato ==========')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\nSaldo: R${saldo:.2f}')
        print('=============================')
    
    elif opcao == 'd':
        break

    else:
        print('Opção inválida, por favor digite a opção desejada novamente')            
            
