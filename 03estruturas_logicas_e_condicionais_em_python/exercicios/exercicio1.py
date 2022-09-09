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

"""
5 Faça um programa que receba um número inteiro e verifique se ele é par ou impar
"""
x = int(input('Digite um número inteiro: '))

if x % 2 == 0:
    print(f'{x} é par')
else:
    print(f'{x} é impar')

"""
6 Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles
assim como a diferença existente entre ambos
"""
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))


if x > y:
    print(f'{x} é maior que {y} e a diferença entre eles é de {x - y}')
elif x ==y:
    print('Os números são iguais e não há diferença entre eles.')
else:
    print(f'{y} é maior que {x} e a diferença entre eles é de {y - x}')

"""
7 Faça um programa que receba dois números e mostre o maior. Se por acaso os dois
números forem iguais, imprima a mensagem Números iguais.
"""
x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

if x > y:
    print(f'O número {x} é o maior')
elif x == y:
    print(f'Números iguais')
else:
    print(f'O número {y} é o maior')

"""
8 Faça um programa que leia 2 notas de um aluno, verifique se as são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente um
valor entre 0.0 e 10.0onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 < 0.0 or nota1 > 10.0 or nota2 < 0.0 or nota2 > 10.0:
    print('Nota invalida')
else:
    print(f' a media é {(nota1 + nota2) / 2}')

"""
9 Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a 
prestação for maior que 20% do salario imprima: Empréstimo não concedido, caso 
constrário imprima> Empréstimo concedido
"""
sal = float(input('Digite o salário: '))
prest = float(input('Digite o valor da prestação: '))

porc_sal = sal * 0.2

if prest < porc_sal:
    print('Empréstimo concedido')
else:
    print('Empréstimo não concedido')

"""
10 Faça um programa que receba a altura e o sexo de uma pessoa, calcule e mostre
o peso ideal, utilizando as seguintes fórmulas (onde h corresponde a altura)
- Homens: (72.7 * h) - 58
- Mulheres: (62.1 * h) - 44.7
"""
altura = float(input('Digite a sua altura: '))
genero = input('Digite seu sexo M/F: ')

if genero == 'F':
    print(f'Sua altura é {altura} e seu peso ideal é {(62.1 * altura) - 44.7}')
elif genero == 'M':
    print(f'Sua altura é {altura} e seu peso ideal é {(72.7 * altura) - 58}')
else:
    print('Sexo inválido')