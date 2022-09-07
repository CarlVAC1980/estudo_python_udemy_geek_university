"""
31 Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
num = int(input('Digite um número inteiro: '))

print(f' o antecessor é {num - 1} e o sucessor é {num + 1}')

"""
32 Leia um número inteiro e imprima a soma do sucessor de seu triplo com antecessor de 
seu dobro.
"""
num = int(input('Digite um número inteiro: '))

triplo = num * 3
dobro = num * 2

soma = (triplo + 1) + (dobro - 1)

print(f'A soma do sucessor de {triplo} com o antecessor de {dobro} é {soma}')

"""
33 Leia o tamanho de um quadrado e imprima como resultado a sua área
"""
lado = float(input('Digite um doa lados de um quadrado: '))

area = lado ** 2

print(f'A área do quadrado é {area}')

"""
34 Leia o valor do raio de um cpírculo e calcule e imprima a área do circulo correspondente.
A área do cículo é pi * raio², considere pi = 3.141592
"""
raio = float(input('Digite o valor do raio do circulo: '))

pi = 3.141592
area = pi * (raio ** 2)

print(f'A área do círculo é {area}')

"""
35 Seja a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = raiz(a² + b³). Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. imprima o resultado dessa operação.
"""
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))

hipotenusa = (a ** 2 + b ** 2) ** (1/2)

print(f'O valor da hipotenusa é {hipotenusa}')
