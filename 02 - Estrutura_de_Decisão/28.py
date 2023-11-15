""" 
28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
 """

carne = int(
    input(
        """
Digite o numero da carne desejada:
    1 - File Duplo
    2 - Alcatra
    3 - Picanha
    Digite aqui: """
    )
)


match carne:
    case 1:
        kilo = float(input("Digite quantos KG deseja: "))
        if kilo <= 5:
            valor = kilo * 4.90
        else:
            valor = kilo * 5.80
        forma_de_pagamento = int(
            input(
        """Qual será a forma de pagamento: 
       1 - cartão Tabajara 5% de desconto
       2 - Dinheiro
       Digite aqui: """
            )
        )
        if forma_de_pagamento == 1:
            desconto = valor * 0.05
            valor_final = valor - desconto
        else:
            valor_final = valor
        print("""Extrato""")
        print("Tipo de  carne: File Duplo ")
        print(f"Quantidade: {kilo:.2f}Kg")
        print(f"Valor total: R${valor:.2f}")
        if forma_de_pagamento == 1: 
            print("Forma de pagamento: Cartão Tabajara")
            print(f"valor do desconto: R${desconto:.2f}")
        elif forma_de_pagamento == 2: 
            print("Forma de pagamento: Dinheiro")        
        print(f"valor a pagar: R${valor_final:.2f}""")

    case 2:
        kilo = float(input("Digite quantos KG deseja: "))
        if kilo <= 5:
            valor = kilo * 5.90
        else:
            valor = kilo * 6.80
        forma_de_pagamento = int(
            input(
        """Qual será a forma de pagamento: 
       1 - cartão Tabajara 5% de desconto
       2 - Dinheiro
       Digite aqui: """
            )
        )
        if forma_de_pagamento == 1:
            desconto = valor * 0.05
            valor_final = valor - desconto
        else:
            valor_final = valor
        print("""Extrato""")
        print("Tipo de  carne: Alcatra")
        print(f"Quantidade: {kilo:.2f}Kg")
        print(f"Valor total: R${valor:.2f}")
        if forma_de_pagamento == 1: 
            print("Forma de pagamento: Cartão Tabajara")
            print(f"valor do desconto: R${desconto:.2f}")
        elif forma_de_pagamento == 2: 
            print("Forma de pagamento: Dinheiro")        
        print(f"valor a pagar: R${valor_final:.2f}""")
    case 3:
        kilo = float(input("Digite quantos KG deseja: "))
        if kilo <= 5:
            valor = kilo * 6.90
        else:
            valor = kilo * 7.80
        forma_de_pagamento = int(
            input(
        """Qual será a forma de pagamento: 
       1 - cartão Tabajara 5% de desconto
       2 - Dinheiro
       Digite aqui: """
            )
        )
        if forma_de_pagamento == 1:
            desconto = valor * 0.05
            valor_final = valor - desconto
        else:
            valor_final = valor
        print("""Extrato""")
        print("Tipo de  carne: Picanha")
        print(f"Quantidade: {kilo:.2f}Kg")
        print(f"Valor total: R${valor:.2f}")
        if forma_de_pagamento == 1: 
            print("Forma de pagamento: Cartão Tabajara")
            print(f"valor do desconto: R${desconto:.2f}")
        elif forma_de_pagamento == 2: 
            print("Forma de pagamento: Dinheiro")        
        print(f"valor a pagar: R${valor_final:.2f}""")
    case _:
        print("Valor invalido programa encerrado!")
