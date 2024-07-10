menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
SAQUES_DIARIOS = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor o qual deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não efetuada. O valor inserido é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor o qual deseja sacar: "))  

        if valor > saldo:
            print("Saldo insuficiente para realizar a operação.")

        elif valor > limite:
            print("Valor limite diário atingido.")

        elif numero_saques >= SAQUES_DIARIOS:
            print("Limite de saques diários atingido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não efetuada. O valor inserido é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma operação das operações diponíveis.")