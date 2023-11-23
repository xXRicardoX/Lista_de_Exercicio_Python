"""
22 - Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""
numero = int(input("digite um valor: "))
if numero < 2:
    print("Não é primo")
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"O numero {numero} é divisivel por {i}")
            print("Não é primo")
            break         
            
       
    else:
        print("É primo")
