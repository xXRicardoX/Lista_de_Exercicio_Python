"""13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido."""

dia_semana = int(input("""Digite um numero referente ao dia da semana
                       1 - Domingo"
                       2 - Segunda
                       3 - Terça
                       4 - Quarta
                       5 - Quinta
                       6 - Sexta
                       7 - Sabado
                       Digite aqui o numero: """))

match dia_semana:
    case 1:
        print ("Hoje é Domingo")
    case 2:
        print ("Hoje é Segunda - Feira")
    case 3:
        print ("Hoje é Terça - Feira")
    case 4:
        print ("Hoje é Quarta - Feira")
    case 5:
        print ("Hoje é Quinta - Feira")
    case 6:
        print ("Hoje é Sexta - Feira")
    case 7:
        print ("Hoje é Sabado")
    case _:
        print ("Valor inválido")