"""
25 - Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
quantidade_pessoas = int(input("Quantidade de pessoas: "))
soma = 0

for i in range(quantidade_pessoas):
    soma += int(input("Digite a idade: "))
media = soma / quantidade_pessoas
print(f"A media de idade é {media:.0f} anos")
if media >= 0 and media <= 25:
    print("Turma jovem")
elif media >= 26 and media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
