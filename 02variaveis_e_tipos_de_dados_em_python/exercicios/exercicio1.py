# 1 Faça um programa que leia um número inteiro e o imprima
numero = 42
print(numero)

# 2 Faça um programa que leia um nuemro real e o imprima
numero = 42.42
print(numero)

# 3 Peça ao usuario para digitar três valores inteiros e imprima a soma deles
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = int(input("Digite o valor de Z: "))

soma = x + y + z

print(f'A soma de {x} + {y} + {z} é {soma}')

# 4 Leia um número real e imprima o resultado do quadrado desse número

x = float(input("Digite um valor real: "))

quadrado = x ** 2

print(f'O valor do quadrado de {x} é {quadrado}')

# 5 Leia um número real e imprima a quinta parte deste número

x = float(input("Digite um valor real: "))

quinta = x / 5

print(f'A quinta parte de {x} é {quinta}')

""" 
6 Leia uma temperatura em graus Celsius e apresente-a convertida em Fahrenheit.
A fórmula de conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenreit
e C a temperatura em Celsius.
"""

c = float(input('Digite a temperatura em Celsius: '))

f = c*(9.0 / 5.0) + 32.0

print(f'A temperatura em Fahrenheit é {f}')


"""
7 Leia uma temperatura em Fahrenheit e apresente-a convertida em Celcius.
A fórmula de conversão é: C=5.0*(F - 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Farenheit
"""
f = float(input('Digite a temperatura em Farenheint: '))

c = 5.0 * (f - 32.0)/ 9.0

print(f'A temperatura em Celsius é {c}')

"""
8 Leia uma temperatura em greus Kelvin e apresente-a convertida em greus Celsius.
A Fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a 
temperatura em Kelvin
"""

k = float(input('Digite um valor em Kelvin: '))

c = k - 273.15

print(f'A temperatura em Celsius é {c}')

"""
9 Leia uma temperatura em graus Celsius e apresente-a em Kelvin.
A Fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

c = float(input('Digite o valor em Celsius: '))

k = c + 273.15

print(f'O valor em Kelvin é {k}')

"""
10 Leia uma velocidade em km/h (quilômetro por hora) e conveerte-a em m/s 
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""

k = float(input('Digite o valor em km/h: '))

m = k/3.6

print(f'A velocidade {k} Km/h convertida em m/s é {m}')
