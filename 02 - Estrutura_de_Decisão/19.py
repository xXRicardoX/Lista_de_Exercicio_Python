"""19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""

numero_inteiro = int(input("Digite um valor: "))

if numero_inteiro <= 1000 and numero_inteiro > 0:
    centena = numero_inteiro // 100
    dezena = (numero_inteiro % 100) // 10
    unidade = numero_inteiro % 10

    resultado = f"{numero_inteiro} = "

    if centena > 0:
        if centena == 0:
            resultado += "1 centena"
        else:
            resultado += f"{centena} centenas"

        if dezena > 0 and unidade > 0:
            resultado += ", "
        elif (dezena > 0 and unidade == 0) or (dezena == 0 and unidade > 0):
            resultado += " e "

    if dezena > 0:
        if dezena == 1:
            resultado += "1 dezena"
        else:
            resultado += f"{dezena} dezenas"

        if unidade > 0:
            resultado += " e "

    if unidade > 0:
        if unidade == 1:
            resultado += "1 unidade"
        else:
            resultado += f"{unidade} unidades"

    print(resultado)


else:
    print("Valor maior que 1000")
