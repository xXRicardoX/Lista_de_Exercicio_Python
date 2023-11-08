"""17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto."""

ano = int(input("Digite um ano para saber se é bissexto ou não: "))

resto4 = ano % 4
resto400 = ano % 400
resto100 = ano % 100


if (resto4 == 0) or (resto400 == 0) and (resto100 != 0):
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não e bissexto:")