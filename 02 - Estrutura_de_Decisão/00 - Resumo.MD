```markdown
# Estrutura de Decisão em Programação

A estrutura de decisão é um conceito fundamental em programação e lógica de computação, permitindo que um programa faça escolhas com base em condições específicas. Ela é frequentemente implementada por meio de instruções condicionais, que direcionam o fluxo do programa com base em testes lógicos.

## Tipos de Estruturas de Decisão

### Declarações Condicionais Simples
Utiliza uma única condição para determinar se uma ação deve ser executada. Por exemplo, em pseudocódigo:

```scss
SE (condição) ENTÃO
     faça algo
FIM SE
```

### Declarações Condicionais Compostas
Envolve a combinação de duas ou mais condições para tomar decisões. Em geral, usa-se uma cláusula se...senão. Por exemplo:

```css
SE (condição) ENTÃO
     faça algo se a condição for verdadeira
SENÃO
     faça outra coisa se a condição for falsa
FIM SE
```

### Declarações Condicionais Aninhadas
Consistem em estruturas de decisão dentro de outras estruturas de decisão. É útil quando se precisa verificar várias condições. Por exemplo:

```scss
SE (condição1) ENTÃO
    SE (condição2) ENTÃO
         faça algo se ambas as condições forem verdadeiras
    FIM SE
SENÃO
     faça outra coisa se a condição1 for falsa
FIM SE
```

### Declarações de Seleção Múltipla (switch-case)
Essas estruturas permitem avaliar uma variável ou expressão e direcionar o fluxo do programa para diferentes seções com base nos valores possíveis. Por exemplo:

```objectivec
ESCOLHA valor
    CASO opção1
         faça algo se valor for igual a opção1
    CASO opção2
         faça outra coisa se valor for igual a opção2
    PADRÃO
         ação padrão se nenhum dos casos anteriores for correspondido
FIM ESCOLHA
```

Essas estruturas são fundamentais para que um programa possa tomar decisões dinâmicas com base em diferentes circunstâncias, permitindo que a lógica do código se adapte e execute ações específicas dependendo das condições estabelecidas.
