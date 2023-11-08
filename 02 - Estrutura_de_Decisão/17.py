"""17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."""

ano = int(input("Digite um ano para saber se é bissexto ou não: "))

if (ano % 4 == 0) or (ano % 400 == 0) and (ano % 100 != 0):
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não e bissexto:")