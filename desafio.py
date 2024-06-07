menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[s] Sair

=>"""

saldo = 200
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito < 0:
            print("Operação inválida. O valor do depósito não pode ser negativo.")  

        else:
           saldo += deposito
           extrato += f"Depósito: R${deposito:.2f}\n"
           print(f"Deposito de R${deposito:.2f} realizado com sucesso!")

    elif opcao == "s":
            saque = float(input("informe o valor do saque:"))

            if numero_saques >= LIMITES_SAQUES:
                    print("Operação inválida. Você já realizou o número máximo de saques diários!")

            elif saque > saldo:
                print("Operação inválida. Saldo insuficiente!")

            elif saque > limite:
                saque = float(input("Operação inválida. O valor do saque excede o limite permitido!"))

            elif saque <= 0:
               print("Operação inválida. O valor do saque deve ser positivo!")

            else:
                saldo -= saque
                extrato += f"Saque: R${saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R${saque:.2f} realizado com sucesso!") 

    elif opcao == "e":
            print("-----------------------Extrato-----------------------")
            print("Nenhuma movimentação." if not extrato else extrato)
            print(f"\nSaldo atual: R${saldo:.2f}")

    elif opcao == "s":
        print('Saindo..')
        break

    else:
        print("Operação invalida, Tente novamente, escolha uma opção!")