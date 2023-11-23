"""
21 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""

numero = int(input("digite um valor: "))


if numero < 2:
    print("Não é primo")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:           
            print("Não é primo")
            break
    else:
        print("É primo")
