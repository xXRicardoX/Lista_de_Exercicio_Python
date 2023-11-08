import math
"""
16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b**2) - (4*a*c)

if a == 0:
    print("O valor de A não pode ser Zero!!!")
elif delta < 0:
    print("O valor da raiz é negativo!!")
elif delta == 0:
    print("Um dos valores da raiz e real")
    x1 = ((-b) + math.sqrt(delta))/ (2 * a)
    x2 = ((-b) - math.sqrt(delta))/ (2 * a)
    print(f"O valor de uma unica  raiz real é x1 = {x1:.2f} e do x2 = {x2:.2f}")
elif delta > 0:
    print("O valor tem duas raizes de valor real")
    x1 = ((-b) + math.sqrt(delta))/ (2 * a)
    x2 = ((-b) - math.sqrt(delta))/ (2 * a)
    print(f"O valor das  raize real é x1 = {x1:.2f} e do x2 = {x2:.2f}")
