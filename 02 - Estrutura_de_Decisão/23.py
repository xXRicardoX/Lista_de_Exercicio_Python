"""
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

informeUmNumero = float(input("Digite um valor: "))


if informeUmNumero != round(informeUmNumero):
    print(f"{informeUmNumero} o valor desse numero e decimal!! ")
else:
    print(f"{round(informeUmNumero)} o valor desse numero e inteiro!!")
