nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <= 10:
    media = (nota1 + nota2) / 2
    print("A media das notas =",media)
elif nota1 < 0 or nota1 > 10:
    print("Nota invalida")
elif nota2 < 0 or nota2 > 10:
    print("Nota invalida")