"""19 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000."""

conjunto_numerico = int(input("Digite a quantidade de valores para somar: "))
soma = 0
if conjunto_numerico >= 0 and conjunto_numerico <= 1000:
    for item in range(conjunto_numerico):
        # Inserindo os valores
        numero = int(input("Digite um numero:"))

        # verificando o maior numero
        if item == 0:
            maior = numero
        else:
            if numero > maior:
                maior = numero
        # Verificando os menores numeros
        if item == 0:
            menor = numero
        else:
            if numero < menor:
                menor = numero
        # Somando os numero digitados
        soma += numero

    print(f"O maior numero é: {maior}")
    print(f"O menor numero é: {menor}")
    print(f"A soma dos numeros é: {soma}")

else:
    print("O numero deve ser maior que zero e menor que 1000")
