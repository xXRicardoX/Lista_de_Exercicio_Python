numero_base = int(input("Digite o valor base: "))
numero_expoente = int(input("Digite o valor do expoente: "))

resutado = 1



for _ in range(numero_expoente):
    resutado *= numero_base
    

print(f"O valor base de {numero_base} elevado a {numero_expoente} é {resutado}")