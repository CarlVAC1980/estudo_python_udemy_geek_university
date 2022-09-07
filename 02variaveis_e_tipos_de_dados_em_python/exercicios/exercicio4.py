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
