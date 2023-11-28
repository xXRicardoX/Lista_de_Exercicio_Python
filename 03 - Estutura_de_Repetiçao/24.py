"""24 - Faça um programa que calcule o mostre a média aritmética de N notas."""


quantidade_media_aritimetica = int(input("Digite a quantidade de notas: "))
soma = 0
for i in range(quantidade_media_aritimetica):
    soma += float(input("Digite a nota: "))
print(f"A média aritimética é {soma / quantidade_media_aritimetica}")
