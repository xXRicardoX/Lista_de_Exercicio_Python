'''8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

produto01 = float(0.55)
produto02 = float(3.49)
produto03 = float(1.44)

if(produto01 < produto02) and (produto01 < produto03):
    print(f"O produto 1 do valor R$ {produto01}, é o mais barato")
elif(produto02 <  produto01) and (produto02 < produto03):
    print(f"O prdouto 2 do valor R$ {produto02},  e o mais barato")
else:
    print(f"O prdouto 3 do valor R$ {produto03},  e o mais barato")