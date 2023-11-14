'''
25 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

numero_1 = float(input("Didite o primeiro valor: "))
numero_2 = float(input("Didite o segundo valor: "))

opção = str(input("""
Escolha um valor abaixo para realizar a operação:
1 - par ou impar
2 - Positivo ou negativo
3 - inteiro ou decimal
Digite aqui: """))

match opção:
    case "1":
        if numero_1 != 0:            
            print(f"O numero {(numero_1)} é impar")
        else:
            print(f"O numero {(numero_1)} é par")
        if numero_2 != 0:
            print(f"O numero {(numero_2)} é impar")
        else:
            print(f"O numero {(numero_2)} é par")
            
    case "2":
        if(numero_1 < 0):
            print(f"O numero {numero_1} é negativo!")
        elif (numero_1 == 0):
            print(f"O numero {numero_1} é neutro!")
        else:
            print(f"O numero {numero_1} é positivo!")
        if(numero_2 < 0):
            print(f"O numero {numero_2} é negativo!")
        elif (numero_2 == 0):
            print(f"O numero {numero_2} é neutro!")
        else:
            print(f"O numero {numero_2} é positivo!")
    case "3":
        if numero_1 != round(numero_1):
            print(f"O valor de {numero_1} é decimal")
        else:
            print(f"O valor de {numero_1} é inteiro")
        if numero_2 != round(numero_2):
            print(f"O valor de {numero_2} é decimal")
        else:
            print(f"O valor de {numero_2} é inteiro")
    case _:
        print("Operação Invalida\nFinalizando o programa")