menu = """

### SISTEMA BANCARIO ###

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
saldo_atual = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = int(input(menu))

    if opcao == 1:
        saldo = float(input("Qual o valor a depositar? "))

        if saldo <= 0:
            print("O valor depositado precisa ser positivo!")
        else:
            saldo_atual = saldo_atual + saldo
            extrato += (f"Deposito Realizado: R$ {saldo:.2f} \n")

    elif opcao == 2:
        saque = int(input("Digite o valor: "))

        if saque <= limite and numero_saques < LIMITE_SAQUES:
            extrato += (f"Saque Realizado: {saque} \n")
            saldo_atual = saldo_atual - saque
            numero_saques = numero_saques + 1
        else:
            print(
                "Você ultrapassou o limite de 500 rais, ou a quanridade de 3 saques por dia!")

    elif opcao == 3:
        print(extrato)
        print(f"Seu saldo atual é de: {saldo_atual}")

    elif opcao == 0:
        print("Obrigado por escolher nossos serviços!! \n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
