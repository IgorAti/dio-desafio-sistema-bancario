
# Menu de opções do cliente
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

# Variáveis iniciais de extrato cliente
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Loop infinito "while = True" dando início ao sistema, finalizando apenas quando selecionada a opção "q" pelo usuário do sistema
while True:
    opcao = input(menu) # Input de opção do cliente

    # Se a opção do cliente for "d", "Depósito", iniciar opcão e solicitar input do valor do depósito ao cliente.
    #  ".lower()" assegura que o "d", input do cliente, tenha formatação minuscula.
    if opcao.lower() == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0: # se valor de depósito maior que 0;
            saldo += valor # atribuir valor de depósito ao saldo;
            extrato += f"Depósito: R$ {valor:.2f}\n" # atribuir informação de depósito ao extrato.

        else: # caso valor informado pelo cliente não seja maior que 0, printar informação de operação não realizada.
            print("Operação não realizada! O valor informado é inválido.")

    # Se a opção do cliente for "s", "Saque", iniciar opcão e solicitar input do valor do saque ao cliente.
    #  ".lower()" assegura que o "s", input do cliente, tenha formatação minuscula.
    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))
        
        if valor > saldo: # se valor input de saque do cliente for maior que o saldo do cliente, printar informação de operação não realizada.
            print("Operação não realizada! Você não tem saldo suficiente.")

        elif valor > limite: # se valor input de saque do cliente for maior que o valor da variável limite, printar informação de operação não realizada.
            print("Operação não realizada! O valor de saque excede o limite permido ao cliente.")

        elif numero_saques >= LIMITE_SAQUES: # se a quantidade de operações de saque "s" for maior que o da constante "LIMITE_SAQUES",
            # printar informação de operação não realizada.
            print("Operação não realizada! Excedido número máximo de saques permitidos ao cliente.")

        elif valor > 0: # se valor de saque form maior que 0;
            saldo -= valor # atribuir negativamente o valor sacado à variável "saldo";
            extrato += f"Saque: R$ {valor:.2f}\n" # atribuir a informação de valor de saque ao extrato.
            numero_saques += 1 # atribuir à variável "numero_saques" +1, contabilizando a quantidade de saques sempre que saque realizado.

        else: # Informar que operação não foi realizada, caso nenhuma das condições do código acima sejam satisfeitas.
            print("Operação não realizada! O valor informado é inválido.")

    # Se a opção do cliente for "e", "Extrato", printar informações de extrato.
    #  ".lower()" assegura que o "e", input do cliente, tenha formatação minuscula.
    elif opcao.lower() == "e":
        print("\n=====================EXTRATO=====================")
        print("Não foram realizadas movimentações." if not extrato else extrato) # Se variável extrato estiver vazia, informar sem movimentações.
        print(f"\nSaldo: R$ {saldo:.2f}") 
        print("==========================================")

    # Se a opção do cliente for "q", "Sair", encerrar rotina sistema.
    #  ".lower()" assegura que o "q", input do cliente, tenha formatação minuscula.
    elif opcao.lower() == "q":
        print("Operação Encerrada") # Printar informação de operação encerrada.
        print("Obrigado por usar nosso sistema!!!")
        break

    # Caso seja realizado qualquer outro input fora das opções, informa opção inválida.
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")