import math

numero = float(input("Informe um numero real ou inteiro: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada do numero",numero,"=",raiz)
else:
    quadrado = math.pow(numero, 2)
    print("O numero",numero,"elevado ao quadrado =",quadrado)