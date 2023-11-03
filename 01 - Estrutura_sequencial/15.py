"""
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    a. salário bruto.
    b. quanto pagou ao INSS.
    c. quanto pagou ao sindicato.
    d.o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
"""

valor_hora_trabalhada = float(input('Digite o valor de horas trabalhadas R$ '))
horas_trabalhada = float(input('Digite a Hora Trabalhada por dia: '))
horas_trabalhada_semanal = horas_trabalhada * 5
horas_trahabalha_mensal = horas_trabalhada_semanal * 4
Salario_mensal = horas_trahabalha_mensal * valor_hora_trabalhada

Salario_bruto = Salario_mensal
imposto_renda = Salario_bruto * 0.11
inss = Salario_bruto * 0.08
sindicato = Salario_bruto * 0.05
valor_desconto = imposto_renda + inss + sindicato
salario_liquido = Salario_bruto - valor_desconto 

print(f'Valor das horas trabalhadas:{valor_hora_trabalhada:.2f}\nValor das horas trabalhadas Mensal: {horas_trahabalha_mensal:.2f}\nO salario Bruto {Salario_bruto:.2f}\nO valor dos impostos de renda: {imposto_renda:.2f}\nValor do INSS {inss}\nO valor do sindicato {sindicato:.2f}\nO valor descontado é - {valor_desconto} Reais\nO salario liquido: {salario_liquido:.2f} Reais')