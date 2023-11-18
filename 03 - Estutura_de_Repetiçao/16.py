atual_valor = 0
proximo_valor = 1

while atual_valor <= 500:
     # Imprimindo o valor atual
    print(atual_valor, end=" ")

    # Atualizando os valores
    novo_valor = atual_valor + proximo_valor
    atual_valor = proximo_valor
    proximo_valor = novo_valor
print(atual_valor, end=" ")
