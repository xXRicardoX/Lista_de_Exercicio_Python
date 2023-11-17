"""
10 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

numero_inicial = int(input("Digite um numero:"))
numero_final = int(input("Digite um numero:"))

if numero_final < numero_inicial:
    numero_inicial, numero_final = numero_final, numero_inicial
    
for cont in range(numero_inicial, numero_final + 1):
    print(cont)