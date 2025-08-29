num1 = float(input("Informe o primeiro numero: "))
num2 = float(input("Informe o outro numero: "))

print("Escolha uma opcao:")
print("1 - Soma de 2 numeros.")
print("2 - Diferenca entre 2 numeros (maior pelo menor).")
print("3 - Produto entre 2 numeros.")
print("4 - Divisao entre 2 numeros (O denominador nao pode ser 0).")
escolha = int(input("Sua opcao: "))

if escolha == 1:
    print("A soma dos 2 numeros =",num1 + num2)
elif escolha == 2:
    if num1 > num2:
        print("A diferenca dos 2 numeros =",num1 - num2)
    else:
        print("A diferenca dos 2 numeros =",num2 - num1)
elif escolha == 3:
    print("O produto dos 2 numeros =",num1 * num2)
elif escolha == 4:
    print("A divisao dos 2 numeros =",num1 / num2)
else:
    print("Escolha invalida.")
