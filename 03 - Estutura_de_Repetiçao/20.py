"""
20 - Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16
"""


while exit != 0:
    numero = int(input("Digite um numero: "))

    if numero < 0:
        print("O fatorial não esta definido para numero negativo!")
    elif numero > 16:
        print("So é aceito valores inteiros menores que 16!")
    else:
        fatorial = 1
        while numero > 1:
            fatorial = fatorial * numero
            numero = numero - 1
        print(f"O valor fatorial é {fatorial}")

    exit = int(input("Digite 0 para sair ou 1 para continuar: "))
