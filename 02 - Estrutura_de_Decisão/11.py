"""
      11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
        Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
        -salários até R$ 280,00 (incluindo) : aumento de 20%
        -salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        -salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        -salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
          o salário antes do reajuste;
          o percentual de aumento aplicado;
          o valor do aumento;
          o novo salário, após o aumento.
"""

salario = float(input("Digite o seu salario: "))

if(salario <= 280.00):
  reajuste = salario * 0.20
  valor_ajustado = reajuste + salario
  print(f"O seu salario atualamente é R$ {salario:.2f} e foi ajustado em 20% teve um aumento de {reajuste:.2f} e foi para um total de R$ {valor_ajustado:.2f}")
  
elif (salario > 280.00) and (salario <= 700.00):
  reajuste = salario * 0.15
  valor_ajustado = reajuste + salario
  print(f"O seu salario atualamente é R$ {salario:.2f} e foi ajustado em 15% teve um aumento de {reajuste:.2f} e foi para um total de R$ {valor_ajustado:.2f}")

elif (salario > 700.00) and (salario <= 1500.00):
  reajuste = salario * 0.10
  valor_ajustado = reajuste + salario
  print(f"O seu salario atualamente é R$ {salario:.2f} e foi ajustado em 10% teve um aumento de {reajuste:.2f} e foi para um total de R$ {valor_ajustado:.2f}")

elif (salario > 1500.00):
  reajuste = salario * 0.05
  valor_ajustado = reajuste + salario
  print(f"O seu salario atualamente é R$ {salario:.2f} e foi ajustado em 5% teve um aumento de {reajuste:.2f} e foi para um total de R$ {valor_ajustado:.2f}")