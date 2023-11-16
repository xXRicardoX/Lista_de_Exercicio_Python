""" 
    04 -Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça  um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
"""
habitanteA = int(80000)
habitanteB = int(200000)

taxaA = float(0.03)
taxaB = float(0.015)

ano = int(0)

while habitanteA < habitanteB:
    habitanteA = habitanteA + (habitanteA * taxaA)
    habitanteB = habitanteB + (habitanteB * taxaB)
    ano = ano + 1

else:
    print(
        f"A quantidade de ano para o habitante A passar a populaçao do habitante B é de {ano} anos."
    )
    