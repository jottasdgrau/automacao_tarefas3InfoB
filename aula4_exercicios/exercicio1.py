''' 
Crie um programa que recebe como entrada dois números reais. 
O programa deve imprimir as quatro operações entre os dois números.
'''

print("Digite o primeiro número: ")
n1 = int(input())

print("Digite o segundo número: ")
n2 = int(input())

divisao = n1/n2
adicao = n1+n2
subtracao = n1-n2
multiplicacao = n1*n2

print("A adição entre eles resulta em: ", adicao)
print("A subtração entre eles resulta em: ", subtracao)
print("A multiplicação entre eles resulta em: ", multiplicacao)
print("A divisão entre eles resulta em: ", divisao)