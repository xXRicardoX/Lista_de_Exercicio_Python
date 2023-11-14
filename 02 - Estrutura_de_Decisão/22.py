'''
    22 - Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''

numero_inteiro = int(input("Digite um valor inteiro: "))
if numero_inteiro % 2 == 0:
    print(f"O numero {numero_inteiro} é par!!")
else:
  print(f"O numero {numero_inteiro} é impar!!")