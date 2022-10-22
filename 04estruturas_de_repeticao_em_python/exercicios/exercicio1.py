"""
1) Faça um programa que determine e mostre os cincos primeiros
múltiplos de 3, considerando números maiores que 0
"""

cont = 0
for i in range(1, 1000):
    if cont >= 5:
        break

    if i % 3 == 0:
        print(i)
        cont += 1
print("Fim exercicio 1")

"""
2) Escreva um prorgama que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes.
A primeira vez deve usar a estrutura de repetição for, a segunda while.
"""

cont = 0
for i in range(1, 101):
    print(i)

print()

cont = 1
while cont <= 100:
    print(cont)
    cont += 1

print("Fim exercicio 2")

"""
3) Faça um algoritmo utilizando o comando while que mostra uma mensagem
regressiva na tela, inciando em 10 e terminando em 0. Mostrar uma mensagem "FIM!"
após a contagem
"""

num = 10
while num >= 0:
    print(num)
    num -= 1

print("FIM!")

print("Fim exercicio 3")

"""
4) Escreva um programa que declare um inteiro, incialize-o com 0,
e incremente-o de 1000 em 1000, imprimindo seu valor na tela,
até que seu valor seja 100000(cem mil).
"""

num = 0

while num < 100000:
    num += 1000
    print(num)

print("Fim exerrcicio 4")

