"""
Crie um programa que execute repetidamente o programa do exercício 2.
Após a apresentação do resultado o programa deve perguntar se o usuário
deseja continuar a calcular, se a resposta for S o programa continua, se for N, o programa termina.
"""
while True:
    print("Digite o primeiro número: ")
    n1 = int(input())

    print("Digite o segundo número: ")
    n2 = int(input())


    print("Escolha o operador: [Digite 1 para adição, 2 para subtração, 3 para divisão e 4 para multiplicação.]")
    operador = int(input())

    divisao = n1/n2
    adicao = n1+n2
    subtracao = n1-n2
    multiplicacao = n1*n2

    if operador == 1:
        print("O resultado de sua pergunta é: ", adicao)
    elif operador == 2:
        print("O resultado de sua pergunta é: ", subtracao)
    elif operador == 3:
        print("O resultado de sua pergunta é: ", divisao)
    elif operador == 4:
        print("O resultado de sua pergunta é: ", multiplicacao)

    print("Deseja continuar? [S = SIM; N = NÃO]")
    resposta = input()

    if resposta == "N":
        break