"""18 - Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores."""

conjunto_numerico = int(input("Digite a quantidade de valores para somar: "))
soma = 0

for item in range(conjunto_numerico):
    # Inserindo os valores
    numero = int(input("Digite um numero:"))
    
    
    # verificando o maior numero
    if item == 0:
        maior = numero
    else:
        if numero > maior:
            maior = numero
    # Verificando os menores numeros
    if item == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero
    # Somando os numero digitados
    soma += numero
    
    
    
print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")
print(f"A soma dos numeros é: {soma}")