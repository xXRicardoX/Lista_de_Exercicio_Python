""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""


import math
from colorama import Fore, Style, init

# Inicializa o colorama para que as cores funcionem no terminal
init()

# Solicita ao usuario o tamanho em m² da area a ser pintada
area_a_ser_pintada = float(input("Informe o tamanho da area a ser pintada em m²: "))

# Define a cobertura de 1 litro de tinta para cada 3 m²
cobertura_por_litro = float(input("Digite a quantidade de cobertura por litro: "))

# Define o tamanho da lata de tinta em litros e o preço da lata
litros_por_lata = float(input("Digite o litro por lata: "))
preco_por_lata = float(input("Digite o preço da lata: "))

# Calcular a quantidade de litros de tinta necessaria
litros_necessario = area_a_ser_pintada / cobertura_por_litro

# Calcular a quantidade de latas de tinta necessárias
latas_necessarias = litros_necessario / litros_por_lata

#arredonda para cima, pois você nãi pode comprar uma fração da lata
latas_necessarias = math.ceil(latas_necessarias)

# Calcula o preço total
preco_total = latas_necessarias * preco_por_lata

# Exibe os resultados para o usuario
print(Fore.GREEN + f"Você precisa de \033[1m{latas_necessarias:.2f} \033[0m" + Fore.GREEN + "latas de tinta")
print(Fore.BLUE + f'O preço total é \033[1mR$ {preco_total:.2f}\033[0m"')
print(Style.RESET_ALL)




