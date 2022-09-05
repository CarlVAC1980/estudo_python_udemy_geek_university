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
