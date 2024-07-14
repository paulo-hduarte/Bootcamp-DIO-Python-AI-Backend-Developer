def menu():
    menu = """\n
    ____________ MENU ____________
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [a] Abrir conta
    [l] Listar contas
    [c] Cadastrar usuário
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação não efetuada. O valor inserido é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, saques_diarios):
    if valor > saldo:
            print("Saldo insuficiente para realizar a operação.")

    elif valor > limite:
            print("Valor acima do limite permitido.")

    elif numero_saques >= saques_diarios:
            print("Limite de saques diários atingido")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(numero_saques)

    else:
            print("Operação não efetuada. O valor inserido é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n________________ EXTRATO ________________")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("__________________________________________")

def cadastar_usuario(usuarios):
    cpf = input("Digite o CPF (somente os números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nUsuário já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário do usuário o qual deseja abrir a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta aberta com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, a conta não foi criada")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("_" * 100)
        print(linha)