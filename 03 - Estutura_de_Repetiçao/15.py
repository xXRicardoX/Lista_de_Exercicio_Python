"""15 - A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,..."""

# Inicializando as variáveis
atual_valor = 0
proximo_valor = 1

# Imprimindo o valor de Fibonacci
print("O valor de Fibonacci é!")
# Loop para imprimir os 10 primeiros valores de Fibonacci
for num in range(10):
    # Imprimindo o valor atual
    print(atual_valor, end=" ")

    # Atualizando os valores
    novo_valor = atual_valor + proximo_valor
    atual_valor = proximo_valor
    proximo_valor = novo_valor
