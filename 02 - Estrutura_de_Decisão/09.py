""" 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente."""
maior = int(input("Digite um numero: "))
meio =  int(input("Digite um numero: "))
menor = int(input("Digite um numero: "))

if(maior > meio) and (maior > menor) and (meio > menor):
    print(f"valor em ordem decrescente em {maior},{meio},{menor}")

if(meio > maior) and (meio > menor) and (maior > menor):
    print(f"valor em ordem decrescente em {meio},{maior},{menor}")

if(menor > maior) and (menor > maior) and ( maior > meio):
    print(f"valor em ordem decrescente em {menor},{maior},{meio}")

if(maior > meio) and (maior > menor) and (menor > meio):
    print(f"valor em ordem decrescente em {maior},{menor},{maior}")

if(meio > maior) and (meio > menor) and (menor > maior):
    print(f"valor em ordem decrescente em {meio},{menor},{maior}")
    
if(menor > maior) and (menor > meio) and (meio > maior):
    print(f"valor em ordem decrescente em {menor},{meio},{maior}")
