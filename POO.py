saldoInicial = 0.0
lista_historico = []

def adcionar_conta():
    global saldoInicial
    print("====Bem-vindo ao Banco sarinhaPVP====")
    nome = input("Por favor, insira seu nome completo:\n ")
    idade = int(input("Por favor, insira sua idade:\n "))
    if idade < 18:
        print("Desculpe, você precisa ser maior de idade para criar uma conta.")
        return False
    else:
        print(f"Conta criada com sucesso! Bem-vindo, {nome}.\n")
        return True
adcionar_conta()

def excluir_conta():
    global saldoInicial
    print("====Excluir Conta====")
    confirmacao = input("Tem certeza que deseja excluir sua conta? (s/n):\n ")
    if confirmacao.lower() == 's':
        saldoInicial = 0.0
        lista_historico.clear()
        print("Conta excluída com sucesso.")
    else:
        print("Operação de exclusão cancelada.")
    return

def depositar():
    global saldoInicial
    print("\n====Depósito====")
    deposito = float(input("Quanto você deseja depositar?:\n "))
    saldoInicial += deposito
    lista_historico.append(f"Depósito: R$ {deposito:.2f}")
    print(f"Depósito de R$ {deposito:.2f} realizado com sucesso! \nSeu saldo atual é R$ {saldoInicial:.2f} \n")
    return

def sacar():
    global saldoInicial
    print("\n====Saque====")
    saque = float(input("Quanto você deseja sacar?:\n "))
    if saque > saldoInicial:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldoInicial -= saque
        lista_historico.append(f"Saque: R$ {saque:.2f}")
        print(f"Saque de R$ {saque:.2f} realizado com sucesso! \nSeu saldo atual é R$ {saldoInicial:.2f} \n")
    return

def ver_saldo_total():
    print("\n====Saldo total====")
    print(f"Seu saldo atual é R$ {saldoInicial:.2f} \n")
    return

def ver_historico():
    print("\n====Histórico de Transações====")
    print("Histórico de transações:")
    if not lista_historico:
        print("Nenhuma transação registrada.")
    else:
        for transacao in lista_historico:
            print(transacao)
    print()
    return

def conceder_emprestimo():
    global saldoInicial
    print("\n====Empréstimo====")
    valor_emprestimo = float(input("Qual o valor do empréstimo que você deseja?:\n "))
    saldoInicial += valor_emprestimo
    lista_historico.append(f"Empréstimo: R$ {valor_emprestimo:.2f}")
    print(f"Empréstimo de R$ {valor_emprestimo:.2f} concedido com sucesso! \nSeu saldo atual é R$ {saldoInicial:.2f} \n")
    return


def menu():
    while True:
        print("=== Menu ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Ver histórico de transações")
        print("5. Excluir conta")
        print("6. Conceder Empréstimo")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            depositar()
        elif opcao == "2":
            sacar()
        elif opcao == "3":
            ver_saldo_total()
        elif opcao == "4":
            ver_historico()
        elif opcao == "5":
            excluir_conta()
            print("Quem sabe algum dia nos encontraremos novamente :( ...")
            break
        elif opcao == "6":
            conceder_emprestimo()
        elif opcao == "7":
            print("Obrigado por usar o Banco sarinhaPVP. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()