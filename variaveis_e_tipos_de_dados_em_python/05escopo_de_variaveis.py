"""
Escopó de Variávais

Dois casos d eescopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas , ou seja, seu escopo
    esta limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variável = valor_de_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existe = 'oi'
print(nao_existe)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # Variável "novo" é um exemplo de variável local
    print(novo)

print(novo)

