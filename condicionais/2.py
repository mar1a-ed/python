import math

numero = int(input("Informe um numero: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz quadrada do numero",numero,"=",raiz,".")
else:
    print("Numero invalido.")