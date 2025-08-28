num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o outro numero: "))

operacao = input("Digite a operacao que deseja fazer (+ soma, - subtracao, x multiplicacao, / divisao): ")

if operacao == '+':
    resultado = num1 + num2
    print("O resultado da soma eh:",resultado)
elif operacao == '-':
    resultado = num1 - num2
    print("O resultado da subtracao eh:",resultado)
elif operacao == 'x':
    resultado = num1 * num2
    print("O resultado da operacao eh:",resultado)
elif operacao == '/':
    resultado = num1 / num2
    print("O resultado da divisao eh:",resultado)
else:
    print("Operacao invalida.")
