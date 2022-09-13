"""
Saindo de loops com break

Funciona daq mesma forma que nas linguagens C ou Java.

Utiulizamos os break para sairmos de loops de maneira projetada.
"""

# Exemplo 1

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop')


# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break