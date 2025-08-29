import math

compras = ["arroz", "carne", "feijao", "miojo", "ovo"]

print("Lista de compras:")

for item in compras:
    print("Produto: ",item)

print("\n")

print("Raizes:")

for i in [1,4,9,16]:
    print("A raiz de",i,"=",math.sqrt(i))

print("\n")

print("Gerando Valores:")

for x in range(5):
    print("Numero =",x + 1)