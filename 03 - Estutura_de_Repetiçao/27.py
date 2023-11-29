"""
27 - Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
"""
quantidade_de_turma = int(input("Digite a quantidade de turma da escola: "))
quantidade_de_aluno = 0

sair = 0
while sair != quantidade_de_turma:
    for i in range(quantidade_de_turma):
        quantidade = int(input("Digite a quantidade de alunos da turma: "))

        if quantidade <= 40:
            quantidade_de_aluno += quantidade
            sair += 1
            if sair == quantidade_de_turma:
                break
        else:
            print("Valor invalido")

media = quantidade_de_aluno / quantidade_de_turma
print(
    f"A media de alunos de {quantidade_de_turma} turmas, com um total de {quantidade_de_aluno} alunos, a media será {media:.2f} alunos por turma"
)
