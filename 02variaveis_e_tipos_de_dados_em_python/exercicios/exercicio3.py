"""
21 Leia o valor da massa em libras e apresente-a convertida em quilosgramas.
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
l = float(input('Digite o valor da massa em libras: '))

k = l * 0.45

print(f'O valor da massa em quilogramas é: {k}')

"""
22 Leia um valor de comprimento em jardas e apresente-o em metros.
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""
j = float(input('Digite um valor em jardas: '))

m = 0.91 * j

print(f'O valor em metros é: {m}')

"""
23 Leia um comprimento em metros e apresente-o em jardas.
A fórmula de conversão é: J = M/0.91, sendo J o comprimento em jardas e M o comprimento em metros.
"""
m = float(input('Digite um valor em metros: '))

j = m / 0.91

print(f'O valor em jardas é: {j}')

"""
24 Leia um valor da área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M * 0.000247, sendo M a área em metros quadrados e
A a área em acres. 
"""
m = float(input('Digite uma area em metros quadrados: '))

a = m * 0.000247

print(f'A área em acres é: {a}')

"""
25 Leia um valor de área em acres e apresente-o convertido em metros quadrados.
A fórmula de conversão é: M = A * 4048,58, sendo M a área em metros quadrados e
A a área em acres.  
"""
a = float(input('Digite a area em acres: '))

m = a * 4048.58

print(f'A área em metros quadrados é: {m}')

"""
26 Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H 
a área em hectares.
"""
m = float(input('Digite a área em metros quadrados: '))

h = m * 0.0001

print(f'O valor em hectares é: {h}')

"""
27 Leia um valor em hectares e apresente-o convertido em metros quadrados.
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H 
a área em hectares.
"""
h = float(input('Digite a área em hectares: '))

m = h * 10000

print(f'O valor em metros quadrados é: {m}')

"""
28 Faça a leitura de três valors e apresente como resultado a soma dos quadrados dos 
três valores lidos
"""
x = float(input('Digite o primeiro valor: '))
y = float(input('Digite o segundo valor: '))
z = float(input('Digite o terceiro valor: '))

result = (x ** 2) + (y ** 2) + ( z ** 2)

print(f'A soma dos quadrados de {x}, {y} e {z} é : {result}')

"""
29 Leia quatro notas, calcule a média aritimetica e imprima o resultado
"""
w = float(input('Digite a primeira nota: '))
x = float(input('Digite a segunda nota: '))
y = float(input('Digite a terceira nota: '))
z = float(input('Digite a quarta nota: '))

media = (w + x + y + z) / 4

print(f'O valor da média das notas é: {media}')

"""
30 Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente 
em dólares.
"""
r = float(input('Digite um valor em real: '))

d = r * 5.45

print(f'O valor em dólares é: ${d}')
