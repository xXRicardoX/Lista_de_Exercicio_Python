# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média

media_1 = float(input("Primeira nota do bimestre: "))
media_2 = float(input("Segunda nota do bimestre: "))
media_3 = float(input("Terceira nota do bimestre: "))
media_4 = float(input("Quarta nota do bimestre: "))

media = (media_1 + media_2 + media_3 + media_4) / 4

print(f'O valor da media é {media:.2f}')