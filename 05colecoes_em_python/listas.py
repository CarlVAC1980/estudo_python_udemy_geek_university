"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você cirar um array do tipo int e tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE o maximo de 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo: Ou seja, podemos criar uma lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fdixo: Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista


