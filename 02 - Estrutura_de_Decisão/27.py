""" 
27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. """

pesoMorango = float(input("Digite o peso do morango: "))
pesoMaca = float(input("Digite o preço da maça: "))

if pesoMorango <= 5:
    valorMorango = pesoMorango * 2.50
else:
    valorMorango = pesoMorango * 2.20
if pesoMaca <= 5:
    valorMaca = pesoMaca * 1.80
else:
    valorMaca = pesoMaca * 1.50

valorTotal = valorMaca + valorMorango
pesoTotal = pesoMaca + pesoMorango

if valorTotal > 25 or pesoTotal > 8:
    valorTotal = valorTotal * 0.9


print(f"O valor total da sua compra sera de R${valorTotal:.2f}")
