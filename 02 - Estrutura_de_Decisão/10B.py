"""10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

nome = str(input("Digite o seu nome: "))
horario = str(input("""Qual o turno que você estuda: 
                    M - matutino
                    V - Vespertino
                    N - Noturno
                    Digite aqui: """)).upper()

match horario:
    case "M":
        print(f"Bom dia!, {nome}")
    case "V":
        print(f"Boa tarde! {nome}")
    case "N":
        print(f"Boa noite {nome}")
    case _:
       print(f" {nome}, vocÊ digitou algo errado verifica a escrita e lembrando que e aceito apenas uma letra") 