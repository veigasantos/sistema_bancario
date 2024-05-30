def exibir_menu():
    # Função que exibe o menu e retorna a opção selecionada.
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    # Adição de strip() e lower() para tratar a entrada do usuário.
    return input(menu).strip().lower()


def realizar_deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        # Utilização de uma lista para armazenar o extrato.
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(
            f"Depósito de R$ {valor:.2f} realizado com sucesso."
        )  # Mensagem de sucesso.
    else:
        print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro.
    return saldo, extrato


def realizar_saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")  # Mensagem de erro.
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")  # Mensagem de erro.
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")  # Mensagem de erro.
    elif valor > 0:
        saldo -= valor
        # Utilização de uma lista para armazenar o extrato.
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")  # Mensagem de sucesso.
    else:
        print("Operação falhou! O valor informado é inválido.")  # Mensagem de erro.

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        # Iteração sobre a lista de extrato para exibição.
        for item in extrato:
            print(item)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    saldo = 0
    limite = 500
    # Utilização de uma lista para armazenar o extrato.
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        # Função que exibe o menu e retorna a opção selecionada.
        opcao = exibir_menu()

        if opcao == "d":
            # Função para realizar depósito.
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "s":
            # Função para realizar saque.
            saldo, extrato, numero_saques = realizar_saque(
                saldo, extrato, numero_saques, limite, LIMITE_SAQUES
            )
        elif opcao == "e":
            # Função para exibir o extrato.
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )  # Mensagem de erro.


# Controle de fluxo principal do programa.
if __name__ == "__main__":
    main()
