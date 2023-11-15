"""1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

valor = int(input("Digite um valor de 0 a 10: "))

while (valor < 0 or valor > 10):
    print("Valor invalido")
    valor = int(input("Digite um valor de 0 a 10: "))
else:
    print(f"O numero digitado é {valor} e esta correto ")