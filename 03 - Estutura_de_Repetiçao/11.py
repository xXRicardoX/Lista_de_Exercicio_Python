""" 11 - Altere o programa anterior para mostrar no final a soma dos números. """


numero_inicial = int(input("Digite um numero inicial: "))
numero_final = int(input("Digite um numero final:"))

soma = 0

if numero_final < numero_inicial:
    numero_inicial, numero_final = numero_final, numero_inicial

for cont in range(numero_inicial, numero_final + 1):
    soma += numero_final
    print(soma)


print(f"Os valores da soma total é {soma}")
