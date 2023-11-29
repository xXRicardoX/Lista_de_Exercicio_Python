"""
28 - Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
quantidade_de_cd = int(input("Quantidade de cd guardado: "))

valor_cd = 0
for i in range(quantidade_de_cd):
    valor_cd += float(input("Digite o valor do cd: R$"))

print("\n")
media = valor_cd / quantidade_de_cd
print(f"O valor total gasto com cd's é {valor_cd} reais\nA media de valor gasto com os cd's é {media:.2f} reais")