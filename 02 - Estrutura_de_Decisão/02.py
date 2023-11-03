'''
    2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

digite_um_valor = int(input("Digite um numero: "))

if (digite_um_valor > 0):
    print(f"O numero digitado {digite_um_valor} é positivo")
elif (digite_um_valor < 0):
    print(f'O numero digitado {digite_um_valor} é negativo')
else:
    print("O valor zero é neutro")
    