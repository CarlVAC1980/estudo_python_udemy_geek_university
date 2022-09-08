"""
1 Faça um programa que receba dois números e mostre qual deles é maior.
"""
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

if x > y:
    print(f'O número {x} é o maior')
elif x == y:
    print(f'Os dois números são iguais')
else:
    print(f'O número {y} é o maior')

"""
2 Leia um número fornecido pelo usuário. Se esse número for positivo , calcule a raiz 
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o 
número é inválido.
"""
num = float(input('Digite um número: '))

if num > 0:
    print(f'A Raiz do número é: {num ** (0.5)}')
else:
    print('Este número é inválido.')

"""
3 Leia um número real. Se o número for positivo imprima a rais quadrada. Do contrátio
imprima o número ao quadrado.
"""
num = float(input('Digite um número: '))

if num > 0:
    print(f'A Raiz do número é: {num ** (0.5)}')
else:
    print(f'O quadrado do número é {num ** 2}')

"""
4 Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado
- A rais quadrada do número digitado
"""
num = float(input('Digite um número: '))

if num > 0:
    print(f'O quadrado do número é {num ** 2}, '
          f'\nA rais quadrada do número é {num **(0.5)}')

