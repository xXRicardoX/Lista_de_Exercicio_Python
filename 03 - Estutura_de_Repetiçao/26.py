""" 
 26 - Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

quantidade_eleitores = int(input("Quantidade de eleitores para votação: "))

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato_nulo = 0
nome_candidato_1 = "Maria Joaquina"
nome_candidato_2 = "Josefina Arantes"
nome_candidato_3 = "Jose carlos"

print("Digite 1 para o candidato 1.\n2 - para o candidato 2\n3 - para cadidato 3")
for i in range(quantidade_eleitores):
    voto = int(input("Digite um numero: "))
    if voto <= 3 and voto > 0:
        if voto == 1:
            candidato1 += 1

        if voto == 2:
            candidato2 += 1

        if voto == 3:
            candidato3 += 1
    else:
        print("O numero não existe!, voto anulado")
        candidato_nulo += 1
print("\n")
if candidato1 > candidato2 and candidato1 > candidato3:
    print(f"O vencedor e do candidato {nome_candidato_1} com seu {candidato1} votos\n")
    print("Os votos dos outros candidatos")
    print(f"voto do candidato {nome_candidato_2}: {candidato2}")
    print(f"voto do candidato {nome_candidato_3}: {candidato3}")
    print(f"Votos nulos: {candidato_nulo}")

elif candidato2 > candidato1 and candidato2 > candidato3:
    print(f"O vencedor e do candidato {nome_candidato_2} com seu {candidato2} votos\n")
    print("Os votos dos outros candidatos")
    print(f"voto do candidato {nome_candidato_1}: {candidato1}")
    print(f"voto do candidato {nome_candidato_3}: {candidato3}")
    print(f"Votos nulos: {candidato_nulo}")

elif candidato3 > candidato1 and candidato3 > candidato2:
    print(f"O vencedor e do candidato {nome_candidato_3} com seu {candidato3} votos\n")
    print("Os votos dos outros candidatos")
    print(f"voto do candidato {nome_candidato_1}: {candidato1}")
    print(f"voto do candidato {nome_candidato_2}: {candidato2}")
    print(f"Votos nulos: {candidato_nulo}")

else:
    print("Empate tecnico por favor consultar os responsaveis!!!")
    print(f"voto do candidato {nome_candidato_1}: {candidato1}")
    print(f"voto do candidato {nome_candidato_2}: {candidato2}")
    print(f"voto do candidato {nome_candidato_3}: {candidato3}")
    print(f"Votos nulos: {candidato_nulo}")
