"""20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
   * A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
   * A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
   * A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

aluno = str(input("Digite o nome do aluno: ")).upper()
nota_1 = int(input("Ditite a primeira nota do aluno: "))
nota_2 = int(input("Ditite a segunda nota do aluno: "))
nota_3 = int(input("Ditite a terceira do aluno: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7 and media < 10:
    print(f"O aluno {aluno} ficou com a media {media:.2f} aprovada")
elif media == 10:
    print(f"O aluno {aluno} ficou com a media {media:.2f} Aprovado com Distinção")
else:
    print(f"O aluno {aluno} ficou com a media {media:.2f} Reprovado")
  

    
    