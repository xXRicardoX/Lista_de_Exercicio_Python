"""
21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valorSaque = int(input("Digite o valor do saque: "))

if 10 <= valorSaque <= 600:
    if valorSaque % 10 != 3:
        duzentoReais = valorSaque // 200 
        cemReais = (valorSaque % 200) // 100
        cinquetaReais = ((valorSaque % 200) % 100) // 50
        dezReais = (((valorSaque % 200) % 100) % 50) // 10
        cincoReais = ((((valorSaque % 200) % 100) % 50) % 10) // 5
        doisReais = (((((valorSaque % 200) % 100) % 50) % 10) % 5) // 2
        
        print(f"O valor informando é {valorSaque} reais\nA quantidade de notas que serão imprimidas será")
        if duzentoReais != 0:
            if duzentoReais == 1:
                print(f'{duzentoReais} nota de duzentos reais')
            else:
                print(f'{duzentoReais} notas de duzentos reais')
            
        if cemReais != 0:
            if cemReais == 1:
                print(f'{cemReais} nota de cem reais')
            else:
                print(f'{cemReais} notas de cem reais')
            
        if cinquetaReais != 0:
            if cinquetaReais == 1:
                print(f"{cinquetaReais} nota de cinquetas reais")
            else:
                print(f"{cinquetaReais} notas de cinquetas reais")
            
        if dezReais != 0:
            if dezReais == 1:
                print(f"{dezReais} nota de dez reais")
            else:
                print(f"{dezReais} notas de dez reais")
        if cincoReais != 0:
            if cincoReais == 1:
                print(f"{cincoReais} nota de cinco reais")
            else:
                print(f"{cincoReais} notas de cinco reais")
        if doisReais != 0:
            if doisReais == 1:
                print(f"{doisReais} nota de dois reais")
            else:
                print(f"{doisReais} notas de dois reais")
    else:
      print("Não imprimimos nota de 1 real\nOperação cancelada")
else:
    print("O caixa não imprimi valor maior que 600 reais e menor que 10 reais!!\nOperação cancelada")