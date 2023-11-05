"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
# inserindo as notas
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a primeira nota: "))
media = (nota_1 + nota_2) / 2
conceito = """Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E"""
print(conceito)
# Verificando a media se foi aprovado ou não
if(media < 0 or media > 10):
    print("Valor da media invalido!!!")
    
elif (media >= 9):
    print(f"""
********boletim****************
A sua nota da P1....{nota_1:.2f}
A sua nota da P2....{nota_2:.2f}
A sua media.........{media:.2f}
Conceito............A""")
    print("Parabens você foi aprovado")
    
elif (media >= 7.5 and media < 9 ):
    print(f"""
********boletim****************
A sua nota da P1....{nota_1:.2f}
A sua nota da P2....{nota_2:.2f}
A sua media.........{media:.2f}
Conceito............B""")
    print("Parabens você foi aprovado")
    
elif (media >= 6):
    print(f"""
********boletim****************
A sua nota da P1....{nota_1:.2f}
A sua nota da P2....{nota_2:.2f}
A sua media.........{media:.2f}
Conceito............C""")
    print("Parabens você foi aprovado")
    
elif (media >= 4):
    print(f"""
********boletim****************
A sua nota da P1....{nota_1:.2f}
A sua nota da P2....{nota_2:.2f}
A sua media.........{media:.2f}
Conceito............D""")
    print("Infelizmente você foi reprovado, nos veremos no proximo ano!!")
    
elif (media >= 0):
    print(f"""
********boletim****************
A sua nota da P1....{nota_1:.2f}
A sua nota da P2....{nota_2:.2f}
A sua media.........{media:.2f}
Conceito............E""")
    print("Infelizmente você foi reprovado, nos veremos no proximo ano!!")
    
    