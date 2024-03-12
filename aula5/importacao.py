"""
Para utilizarmos as funções criadas em outros
arquivos de código fonte devemos importá-las. Para 
isso uilizamos o comando import ou from import.
"""
#Exemplo 1 - Importar todas funções

import funcao

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

area = funcao.calcularAreaTriangulo(base,altura)
print(area)