"""
26 -Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
b. até 20 litros, desconto de 3% por litro
c. acima de 20 litros, desconto de 5% por litro

d. Gasolina:
e. até 20 litros, desconto de 4% por litro
f.acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

combustivel = str(
    input(
        """
Qual combustivel vai utilizar:
G - Gasolina
A - álcool
Digite aqui a letra: """
    )
).lower()
litros = float(input("Quantos litros vai abastecer?: "))
gasolina = 2.50
alcool = 1.90
match combustivel:
    case "g":
        if litros <= 20:
            valor = (litros * gasolina) * 1.04
            print(f"O valor total a pagar da gasolina é: R$ {valor:.2f}")
        else:
            valor = (litros * gasolina) * 1.06
            print(f"O valor total a pagar da gasolina é: R$ {valor:.2f}")
    case "a":
        if litros <= 20:
            valor = (litros * alcool) * 1.04
            print(f"O valor total a pagar do álcool é: R$ {valor:.2f}")
        else:
            valor = (litros * alcool) * 1.06
            print(f"O valor total a pagar do álcool é: R$ {valor:.2f}")
    case _:
        print("Digite A para álcool e G para gasolina\nPrograma encerrado")
