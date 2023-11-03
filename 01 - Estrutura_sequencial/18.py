"""
    18 -  Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

tamanho_do_arquivo = float(input("Digite o tamanho do arquivo: "))
velocidade_download = float(input("Digite a velocidade da internet: "))

tempo_estimado_segundos = tamanho_do_arquivo / (velocidade_download / 8)

tempo_estimado_min = tempo_estimado_segundos / 60

print(f'O tempo estimado de um arquivo de {tamanho_do_arquivo:.2f} mb de uma velocidade de internet {velocidade_download:.2f} mb/s sera em {tempo_estimado_min:.2f} min')