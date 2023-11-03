""" 6 - Faça um Programa que leia três números e mostre o maior deles."""
 
numero_1 = int(input("Digite o valor do numero 1: "))
numero_2 = int(input("Digite o valor do numero 2: "))
numero_3 = int(input("Digite o valor do numero 3: "))

if(numero_1 > numero_2) and (numero_1 > numero_3):
    print("O valor do numero 1 e o maior valor")
    print(numero_1)
elif(numero_2 > numero_1) and (numero_2 > numero_3):
    print("O valor do numero numero 2 e o maior valor")
    print(numero_2)
else:
    print("O valor do numero numero 3 é o maior valor")
    print(numero_3)
    

    
     