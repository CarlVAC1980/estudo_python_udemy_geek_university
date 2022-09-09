"""
11 Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algorismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com
a mensagem "Número inválido".
"""
x = int(input('Digite um número inteiro maior que zero: '))

if x < 0:
    print('Número inválido')
else:
    soma = 0
    y = str(x)
    for i in range(len(y)):
        soma += int(y[i])
    print(soma)

"""
12 Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número 
inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
