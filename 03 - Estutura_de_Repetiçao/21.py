

numero = int(input("Digite um numero para verificar se são numeros primos ou não: "))

if numero <= 1:
    print("não são numeros primos")
else:
    for item in range(2, numero):
        if numero % item == 0:
            print("não são numeros primos")
            break   
        else:
            print("são numeros primos")
            break