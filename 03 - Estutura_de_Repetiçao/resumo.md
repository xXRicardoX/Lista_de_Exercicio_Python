# Estruturas de Repetição em Python

## 1. For Loop

O loop `for` é utilizado para iterar sobre elementos em uma sequência (como listas, tuplas, strings ou intervalos numéricos).

### Sintaxe:

```python
for elemento in sequencia:
    # código a ser repetido para cada elemento na sequência
    print(elemento)

Exemplo com intervalo numérico:
for i in range(5):
    # código a ser repetido 5 vezes, com i variando de 0 a 4
    print(i)

Iteração Direta: O loop for percorre diretamente os elementos da sequência, tornando-o útil quando você precisa acessar cada item.
2. While Loop
O loop while executa um bloco de código enquanto uma condição específica for verdadeira.

### Sintaxe:

while condição:
    # código a ser repetido enquanto a condição for verdadeira
    print("Executando enquanto a condição é verdadeira.")

Exemplo:
contador = 0
while contador < 5:
    # código a ser repetido enquanto a condição for verdadeira
    print(contador)
    contador += 1  # Importante incrementar o contador para evitar um loop infinito

Observações Importantes:

Evitar Loops Infinitos: Certifique-se de que a condição eventualmente se torne falsa para evitar loops infinitos.
Atualização da Variável de Controle: Em loops while, é crucial atualizar a variável de controle dentro do loop para evitar a execução indefinida.
Estas estruturas oferecem flexibilidade na execução de operações repetitivas em Python, e a escolha entre elas depende do contexto específico do problema que você está resolvendo.
```