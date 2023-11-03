""" 
    11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo. """

n1 = int(15)
n2 = int(45)
n3 = float(65.1)

produto = (n1 * 2) * (n2/2)
soma = (n1 * 3) + n3
cubo = n3**3

print("O produto do dobro do primeiro da metade do seundo é ", produto)

print("A soma do triplo do primeiro com o terceiro é ", soma)

print(f'O terceiro elevado ao cubo é {cubo:.2f}')
