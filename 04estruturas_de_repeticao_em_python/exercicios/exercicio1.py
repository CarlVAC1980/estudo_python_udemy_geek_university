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

"""
5) Faça um programa que peça ao usuário para digitar
10 valores e some-os.
"""

soma = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}° valor: "))
    soma += num

print()
print(soma)

print("Fim exercicio 5")

"""
6) Faça um programa que leia 10 inteiros e imprima sua média.
"""

media = 0
for i in range(1, 11):
    num = int(input(f"Digite o {i}° valor: "))
    media += num
    if i >= 10:
        media = media/i

print()
print(f"Média: {media}")

print("Fim exercicio 6")

"""
7) Faça um programa que leia 10 inteiros positivos, ignorando não positivos,
e imprima sua média
"""
media = 0
soma = 0
count = 10

for i in range(1, 11):
    num = int(input(f"Digite o {i}º valor: "))
    if num < 0:
        count -= 1
    else:
        soma += num

    if i >= 10:
        media = soma / count
print(f"A média é: {media}")

print("Fim exercicio 7")

"""
8) Escreva um programa que leia 10 números e escreva o menor
valor lido e o maior valor lido.
"""

menor = 0
maior = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}° valor: "))
    if menor == 0 and maior ==0:
        menor = num
        maior = num
    elif menor > num:
        menor = num
    elif maior < num:
        maior = num

print(f"O menor é {menor} e o maior é {maior}.")

print('Fim exercicio 8')

"""
9) Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímpares
"""
n = int(input("digite um número: "))
impar = 0
cont = 0

for i in range(1, n*n):
    if i % 2 ==1:
        print(i)
        cont += 1
    if cont >= n:
        break

print("Fim exercicio 9")

"""
10) Faça um programa que calcule e mostre a soma dos 50
primeiros números pares.
"""
n = 50
par = 0
cont = 0

for i in range(1, 1000):
    if i % 2 == 0:
        print(i)
        par += i
        cont += 1
    if cont >= 50:
        break
print(f"A soma dos números é {par}")

print("Fim exercicico 10")

