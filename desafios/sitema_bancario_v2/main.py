from sistema_bancario_v2 import *

AGENCIA = "0001"
SAQUES_DIARIOS = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor o qual deseja depositar: "))

        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "s":
        valor = float(input("Informe o valor o qual deseja sacar: "))

        saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,saques_diarios=SAQUES_DIARIOS,)
        numero_saques += 1
          
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        cadastar_usuario(usuarios)
    
    elif opcao == "a":
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
                contas.append(conta)

    elif opcao == "l":
         listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione uma operação das operações diponíveis.")