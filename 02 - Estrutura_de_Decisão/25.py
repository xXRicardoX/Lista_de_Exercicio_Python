""" 
25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
 """

print("As respostas so pode ser sim ou não")
pergunta1 = input("Telefonou para a vítima? ").lower()
pergunta2 = input("Esteve no local do crime? ").lower()
pergunta3 = input("Mora perto da vítima? ").lower()
pergunta4 = input("Devia para a vítima? ").lower()

if (
    pergunta1 == "sim"
    or pergunta2 == "sim"
    or pergunta3 == "sim"
    or pergunta4 == "sim"
    or pergunta1 == "não"
    or pergunta2 == "não"
    or pergunta3 == "não"
    or pergunta4 == "não"
):
    if (
        pergunta1 == "sim"
        and pergunta2 == "sim"
        and pergunta3 == "sim"
        and pergunta4 == "sim"
    ):
        print("Assassino")

    elif (
        pergunta1 == "sim"
        and pergunta2 == "sim"
        and pergunta3 == "sim"
        or pergunta1 == "sim"
        and pergunta2 == "sim"
        and pergunta4 == "sim"
        or pergunta1 == "sim"
        and pergunta4 == "sim"
        and pergunta3 == "sim"
        or pergunta4 == "sim"
        and pergunta2 == "sim"
        and pergunta3 == "sim"
    ):
        print("Cúmplice")

    elif (
        pergunta1 == "sim"
        and pergunta2 == "sim"
        or pergunta1 == "sim"
        and pergunta3 == "sim"
        or pergunta3 == "sim"
        and pergunta2 == "sim"
        or pergunta4 == "sim"
        and pergunta2 == "sim"
        or pergunta3 == "sim"
        and pergunta4 == "sim"
        or pergunta1 == "sim"
        and pergunta4 == "sim"
    ):
        print("Suspeita")
    else:
        print("Inocente")
else:
    print("Resposta invalida")
