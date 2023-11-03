""" 
    14 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
 """

peso_peixe = float(input("Digite o valor do peso do peixe: "))

if peso_peixe > 50 and peso_peixe >= 0:
    valor_multa = 4.00
    peso_excedente =  peso_peixe - 50
    print(f'O peso do peixe é {peso_peixe:.2f} kg\nO peso excedeu em {peso_excedente:.2f} Kg\nO valor da multa é {valor_multa} Reais\nO valor será cobrado é {peso_excedente * valor_multa:.2f} Reais')
elif peso_peixe <= 50 and peso_peixe >= 0:
    print(f'O peso do peixe {peso_peixe:.2f} Kg está abaixo ou igual do regulamento do estado de São Paulo!')
else:
    print("Houve um erro na digitação, fim do programa")