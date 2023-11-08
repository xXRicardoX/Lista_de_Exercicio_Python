"""18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = input("Digite uma data no formato de dd/mm/aaa: ")

try:
    dia, mes, ano = map(int, data.split('/'))
    data_valida = True
    if not(1 <= mes <= 12):
        data_valida = False
    elif mes in (1,3,5,7,8,10,12):
        if not(1 <= dia <= 31):
            data_valida = False
    elif mes in (4,6,9,11):
        data_valida = False
    elif mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            if not(1 <= dia <= 29):
                data_valida = False
        else:
            if not(1 <= dia <=28):
                data_valida = False
    else:
        data_valida = False
    
    if data_valida:
        print("A data é valida!!!")
    else:
        print("A data é invalida")
except(ValueError, IndexError):
    print("Formato de data inválido. Use dd/mm/aaaa.")