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

"""
36 Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O Volume 
de um cilindro circular é calculado por meio da seguinte fórmula: V = PI * R² * altura, 
onde pi = 3.141592.
"""
r = float(input('Digite o valor do raio: '))
a = float(input('Digite o valor da altura: '))

pi = 3.141592
v = pi * r ** 2 * a

print(f'O volume do cilindro é {v}')

"""
37 Faça um programa que leia o valor de um produto e imprima o valor com desconto , tendo
em vista que o desconto foi de 12%
"""
p = float(input('Digite o valor de um produto: '))

d = p * 12/100
vf = p - d

print(f'Valor do produto com desconto {vf}')

"""
38 Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que 
ele recebeu um aumento de 25%.
"""
s = float(input('Digite o valor do salário atual: '))

a = s * 25/100
ns = s + a

print(f'O valor do salário novo é {ns}')

"""
39 A importância de R$ 780 000.00 será dividida entre ganhadores de um concurso.
Sendo que da quantia total:
 - O primeiro ganhador receberá 46%
 - O segundo receberá 32%
- O terceiro receberá o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores do premio.
"""
p = 780000.00

p1 = p * 46/100
p2 = p * 32/100
p3 = p - (p1 + p2)

print(f'O primeiro ganhador receberá R$ {p1}, \no segundo ganhardo receberá R$ {p2} \ne o terceiro ganhador receberá R$ {p3}')

"""
40 Uma empresa contrata um encanador por R$ 30.00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia liquida que deverá ser 
paga, sabendo-se que são descontados 8% para imposto de renda.
"""
d = float(input('Digite a quantidade de dias trabalhados: '))

bruto = d * 30.00
liquido = bruto * 0.92

print(f'Valor bruto R$ {bruto}, valor liquido já comd esconto de 8% R$ {liquido}')
