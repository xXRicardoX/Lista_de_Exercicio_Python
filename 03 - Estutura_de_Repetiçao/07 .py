# 07 - Faça um programa que leia 5 números e informe o maior número.

for item in range(5):
    numero = int(input("Digite um numero:"))
    if item == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
print(f"O maior numero é: {maior}")
