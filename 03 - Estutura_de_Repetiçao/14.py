par = 0
impar = 0

for i in range(10):
    numero_inteiro = int(input('Digite um número inteiro: '))
    if numero_inteiro % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Você digitou {par} números pares e {impar} números ímpares.')