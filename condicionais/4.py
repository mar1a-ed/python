import math

num = float(input("Insira um numero qualquer: "))

raiz = math.sqrt(num)
quadrado = math.pow(num, 2)

if num >= 0:
    print("A raiz quadrada do numero",num,"=",raiz,"e o proprio elevado ao quadrado =",quadrado)
else:
    print("Numero invalido para calculo.")