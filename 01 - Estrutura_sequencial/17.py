""" 
17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
a - comprar apenas latas de 18 litros;
b - comprar apenas galões de 3,6 litros;
c  -misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. """


import math
from colorama import Fore, Style, init

init()


area_a_ser_pintada = float(input("Digite a area a ser pintada em m²: "))
cobertura_por_litro = 6

print(
    """Escolha uma opção
                           1 - lata de tinta 
                           2 - galões de tinta """
)
escolher_opção = int(input())
if escolher_opção == 1:
    litros_por_lata = 18
    preco_por_lata = 80.00
    litros_necessarios = area_a_ser_pintada / cobertura_por_litro

    latas_necessaria = (litros_necessarios / litros_por_lata) * 1.10

    latas_necessarias = math.ceil(latas_necessaria)
    preco_total_lata = latas_necessarias * preco_por_lata

    print(
        Fore.GREEN
        + f"Voce precisa de \033[1m{latas_necessarias:.2f}\033[0m "
        + Fore.GREEN
        + "latas de tinta ja acrescentado os 10 porcento de folga"
    )
    print(Fore.BLUE + f"O preço total é \033[1mR$ {preco_total_lata:.2f}\033[0m")
    print(Style.RESET_ALL)


elif escolher_opção == 2:
    galões_de_tinta_por_litros = 3.60
    preco_galões_tinta = 25.00

    litros_necessarios = area_a_ser_pintada / cobertura_por_litro
    litros_de_galoes_necessarios = (
        litros_necessarios / galões_de_tinta_por_litros
    ) * 1.10
    litros_de_galoes_necessarios = math.ceil(litros_de_galoes_necessarios)
    preco_total_galoes = litros_de_galoes_necessarios * preco_galões_tinta

    print(
        Fore.GREEN
        + f"Voce precisa de \033[1m{litros_de_galoes_necessarios:.2f}\033[0m "
        + Fore.GREEN
        + "galões de tinta ja acrescentado os 10 porcento de folga"
    )
    print(Fore.BLUE + f"O preço total é \033[1mR$ {preco_total_galoes:.2f}\033[0m")
    print(Style.RESET_ALL)
