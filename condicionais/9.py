salario = float(input("Informe o valor do salario: "))
emprestimo = float(input("Informe o valor do emprestimo: "))

percento = (20 * salario) / 100;

if emprestimo > percento:
    print("Emprestimo nao concedido.")
else:
    print("Emprestimo concedido.")