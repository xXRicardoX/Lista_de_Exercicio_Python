#  8 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora_trabalhada = float(input('Digite o valor de horas trabalhadas R$ ' ))
horas_trabalhada = float(input('Digite a Hora Trabalhada por dia: '))
horas_trabalhada_semanal = horas_trabalhada * 5

print(f'valor da hora trabalha semanal {horas_trabalhada_semanal} horas')

horas_trahabalha_mensal = horas_trabalhada_semanal * 4

Salario_mensal = horas_trahabalha_mensal * valor_hora_trabalhada

print(f'O valor das horas trabalhadas {valor_hora_trabalhada:.2f} Reais.\nHoras trabalhadas no mes {horas_trahabalha_mensal} horas.\nSalario do mês {Salario_mensal:.2f} Reais')
