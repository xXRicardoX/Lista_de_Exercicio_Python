'''3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido'''

sexo = str(input("""
                 Digite a letra do seu sexo:
                 F - para Feminino
                 M - para masculino
                 """)).upper()

if (sexo == 'F'):
    print("Seu sexo e Feminino")
elif(sexo == "M"):
    print("Seu sexo é masculino")
else:
    print("Sexo invalido!!")
