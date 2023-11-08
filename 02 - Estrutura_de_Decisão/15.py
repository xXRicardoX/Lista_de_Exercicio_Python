"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""

print("Digite os lados do triangulo")
lado_a = int(input("Dgitie o lado A: "))
lado_b = int(input("Dgitie o lado B: "))
lado_c = int(input("Dgitie o lado C: "))

if(lado_a == lado_b and lado_a == lado_c and lado_b == lado_c):
    print("Os tres lado  do triangulo são iguais então o triangulo é equilátero")
elif(lado_a == lado_b or lado_b == lado_c or lado_a == lado_c):
    print("Os dois lados do triangulo são iguais então o triangulo é isósceles")
else:
    print("Nenhum dos lados do triangulo são iguais então o triangulo é escaleno")
    