"""08 - Faça um programa que leia 5 números e informe a soma e a média dos números."""

valor = 0

for cont in range(1, 6):
    numero = int(input("Digite um numero:"))
    valor += numero

print(valor)
media = valor / 5
print(f"A media é: {media:.2f}")
