"""
05 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""
sair = 1

while sair != 0:
    

    habitanteA = int(input("Digite a quantidade de população da cidade A: "))
    habitanteB = int(input("Digite a quantidade de populaçao da cidade B:"))

    valor_taxaA = float(input("Digite o valor da taxa de crescimento da cidade A: "))
    valor_taxaB = float(input("Digite o valor da taxa de crescimento da cidade B: "))
    taxaA = float(valor_taxaA / 100)
    taxaB = float(valor_taxaB / 100)

    ano = int(0)

    while(habitanteA < habitanteB):
        habitanteA = habitanteA + (habitanteA * taxaA)  
        habitanteB = habitanteB + (habitanteB * taxaB)
        ano = ano + 1
        

    else:
        print(f"A quantidade de ano para o habitante A passar a populaçao do habitante B é de {ano} anos.")
        sair = int(input("Digite 0 para sair ou 1 para continuar: "))
        print("\n")
print("Programa Encerrado")