# 9 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).

f = float(input('Digite o valor da temperatura em fahrenheit '))

c = 5 * ((f - 32) / 9)

print(f'A tempretatura de {f:.2f} °F.\nTemperatura em {c:.2f} °C')