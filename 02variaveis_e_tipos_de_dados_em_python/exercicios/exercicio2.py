"""
11 Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetro por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M m/s
"""
m = float(input('Digite o valor em metros por segundo: '))

k = m * 3.6

print(f'O valor em quilometrôs por hora é de {k}')

"""
12 Leia a distância em milhas e apresente-a convertida em quilometros. A fórmula de 
covnersão é: K = 1.61 * M, sendo K a distância em quilometros e M a distância em milhas
"""
m = float(input('Digite o valor em milhas: '))

k = 1.61 * m

print(f'O valor em quilometros é: {k}')

"""
13 Leia a distancia em quilometros e apresente-a convertida em milhas. A Fórmula de 
conversão é: M = K/1.61, sendo K a distância em quilometros e M a distância em milhas
"""
k = float(input('Digite o valor em quilometros: '))

m = k/1.61

print(f'O valor em milhas é: {m}')

"""
14 Leia um ângulo em graus e apresente-o convertido em radianos. A fómula de conversão 
é: R = G*pi/180, sendo G o ângulo em graus e R em radianos e pi = 3,14
"""
g = float(input('Digite o ângulo em graus: '))

pi = 3.14
r = g * pi / 180

print(f'O valor do ânmgulo em radianos é: {r}')

"""
15 Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de ceronveersão 
é: G = R*180/pi, sendo G o ângulo em graus e R em radianos e pi = 3,14
"""
r = float(input('Digite o ângulo em radianos: '))

pi = 3.14
g = r * 180 / pi

print(f'O valor do ângulo em graus é: {g}')

"""
16 Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centimetros e P o 
copmpirmento em polegadas.
"""
p = float(input('Digite um valor em polegadas: '))

c = p * 2.54

print(f'O valor em centimetros é: {c}')
"""
17 Leia um valor de comprimento em centimentros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2.54 
"""
c = float(input('Digite um valor em centimentros: '))

p = c/2.54

print(f'o valor em polegadas é: {p}')

"""
18 Leia um valor de volume em metros cubicos m³ e apresente-o convertido em Litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos
"""
m = float(input('Digite um valor em metros cúbicos: '))

l = 1000 * m

print(f'O valor em litros é: {l}')
"""
19 Leia um valor de volume em Litros e apresente-o convertido em metros cúbicos.
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em
metros cúbicos
"""
l = float(input('Digite um valor em litros: '))

m = l/1000

print(f'O valor em metros cúbicos é: {m}')

"""
20 Leia um valor de massa em quilogramas e apresente-o em libras. A fórmula 
de conversão é: L = K/0.45, sendo K a massa em quilogramas e l a massa em libras
"""
k = float(input('Digite o valor em quilogramas: '))

l = k / 0.45

print(f'O valor em libras é: {l}')
