""" 
23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""

numero_primos = int(input("Digite um número: "))

print(f"Os números primos de 0 a {numero_primos} são: ", end="")

for i in range(numero_primos + 1):
    if i < 2:
        continue
    else:
        primo = i
        for primo in range(2, int(primo**0.5) + 1):
            if i % primo == 0:
                break
        else:
            print(i, end=" ")
