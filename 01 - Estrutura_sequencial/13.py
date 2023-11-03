""" 
    13 Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7 """

altura = float(input("Digite a sua altura: "))

sexo = str(input("Digite F para feminino ou M para masculino: ")).upper()

if sexo == "F":
    peso_ideal_feminino = (62.1 * altura) - 44.7
    print(f'A sua altura é {altura:.2f} o seu peso ideal é  {peso_ideal_feminino:.2f}Kg feminino')
elif sexo == "M":
    peso_ideal_masculino = (72.7 * altura) - 58
    print(f'A sua altura é {altura:.2f} o seu peso ideal é {peso_ideal_masculino:.2f}Kg')
else:
    print("Voce digitou algo errado, fim do programa")
    