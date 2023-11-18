"""
17 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 
"""

numero = int(input('Digite um numero: '))

if numero < 0:
    print('O fatorial não esta definido para numero negativo!')
else:
    fatorial = 1
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1        
    print(f"O valor fatorial é {fatorial}")