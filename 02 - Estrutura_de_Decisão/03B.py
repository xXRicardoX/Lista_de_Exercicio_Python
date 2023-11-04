'''3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido'''

sexo = str(input("""
                 Digite a letra do seu sexo:
                 F - para Feminino
                 M - para masculino
                 Digite aqui a Letra F ou M: """)).upper()

match sexo:
    case "F":
        print("Seu sexo e Feminino!")
    case "M":
        print("Seu sexo e Masculino!")
    case _:
        print("Sexo invalido!!")