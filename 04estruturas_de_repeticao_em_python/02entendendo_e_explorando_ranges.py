"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com o loop for

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo de 1 em 1)

# Exemplo Forma 2

for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 3
for num in range(0, 55, 5):
    print(num)

# Forma 4 (Inversa - regressiva)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo Forma 4
for num in range(10, -1, -1):
    print(num)
"""

