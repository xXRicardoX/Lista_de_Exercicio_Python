"""
23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""

informeUmNumero = float(input("Digite um valor: "))
informeUmNumeroInteiro = round(informeUmNumero)

if informeUmNumero != informeUmNumeroInteiro:
    print(f"{informeUmNumero} o valor desse numero e decimal!! ")
else:
    print(f"{informeUmNumeroInteiro} o valor desse numero e inteiro!!")
