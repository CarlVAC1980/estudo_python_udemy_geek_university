"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: o separador de casas decimais na programação é o ponto e não a virgula
"""

# Errado do ponto de vista fo float, mas gera uma tupla
valor = 1, 44

print(valor)
print(type(valor))

# Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

# É possivél fazer
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float par aum int
"""
OBS = ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j
