"""
21 Escreva o menu de operações abaixo. Leia a opção do usuário e execute a operação
escolhida. nEscreva uma mensagem de erro se a opção foi inválida.
"""
print('Escolha a opção: '
      '\n 1 - Soma de 2 núemros. '
      '\n 2 - Diferença entre 2 números (maior pelo menor). '
      '\n 3 - Produto entre 2 números. '
      '\n 4 - Divisão entre 2 números (o denominador não pode ser zero). ')
op = int((input('Opção: ')))

x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))

match op:
    case 1:
        print(f'A soma de {x} e {y} é {x + y}')
    case 2:
        if x > y:
            print(f'A diferenteça entre {x} e {y} é {x - y}')
        else:
            print(f'A diferença entre {y} e {x} é {y - x}')
    case 3:
        print(f'O produto entre {x} e {y} é {x * y}')
    case 4:
        if y == 0:
            print('Denominador igual a zero, operação inválida')
        else:
            print(f'A divisão entre {x} e {y} é {x / y}')
    case _:
        print('Opção inválida')

"""
22 Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não pode se 
aposentar. As condições para aposentadoria são:
- Ter pelo menos 65 anos,
- Ou ter trabalhado pelo menos 30 anos,
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = int(input('Digite a idade: '))
tempo = int(input('Digite quanto tempo de serviço em anos: '))

if idade >= 65:
    print('Pode se aposentar.')
elif tempo >= 30:
    print('Pode se aposentar.')

if idade >= 60 and tempo >= 25:
    print('Pode se aposentar.')
else:
    print('Não pode se aposentar')

"""
23 Determine se um determinado ano lido é bisexto. Sendo que um ano é bisexto se 
for divisível por 400 ou se for divisível por 4 e não divisível por 100. Por exemplo
1988, 1992, 1996
"""
ano = int(input('Digite um ano completo, com os todos os seus digitos: '))

if (ano % 400 == 0 or ano % 4 == 0) and ano % 100 != 0:
    print('Ano Bisexto')
else:
    print('Ano não Bisexto')

"""24 Uma empresa vende o mesmo produto para quatro estados diferentes. Cada estado 
possui uma taxa diferente de imposto sobre o produto(MG 7%; SP 12%; RJ 15%; MS 8%). 
Faça um programa em que o usuário entre com o valor e o estado destino do 
produto e o programa retorne o preçlo final do produto acrescido do imposto do estado 
em que será vencido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""

produto = float(input('Digite o valor do produto: '))
estado = input('Digite o estado para onde o produto vai (MG, SP, RJ, MS): ')

match estado:
    case 'MG':
        print(f'O valor do produto mais 7% de imposto é {produto + (produto * 0.07)}')
    case 'SP':
        print(f'O valor do produto mais 12% de imposto é {produto + (produto * 0.12)}')
    case 'RJ':
        print(f'O valor do produto mais 12% de imposto é {produto + (produto * 0.15)}')
    case 'MS':
        print(f'O valor do produto mais 12% de imposto é {produto + (produto * 0.08)}')
    case _:
        print('Estado digitado inválido')

"""
25 Calcule as raízes da equação de 2º grau. Lembrando que: x = (-b +- rais de delta) / 2a 
onde delta = B² - 4ac. E (a*x)² + (b *x) + c = 0 respresenta uma equação de segundo gra.
A variável a ten  que ser diferente de zero. Caso seja igual imprima a mensagem 
"Não é equação de segundo grau"
 - Se delta for menor que  zero, não existe raiz real. Imprima a mensagem "Não existe raiz"
 - Se delta for igual a zero, existe uma raiz real. Imrpima a raiz e a mensagem "Raiz unica"
 - Se delta for maior ou igual, imprima as duas raizes reais. 
"""
import math

print('Equação de segundo grau da forma: ax² + bx + c')

a = float(input('Coeficiente a: '))
if (a == 0):
    print('Não é equação de segundo grau')
else:
    b = float(input('Coeficiente b: '))
    c = float(input('Coeficiente c: '))
    delta = (b**2) - (4 * a * c)

    if delta < 0:
        print('Não existe raiz')
    elif delta == 0:
        raiz = - b / (2 * a)
        print(f'Raiz unica. A raiz é {raiz}')
    else:
        raiz1 = (- b + math.sqrt(delta)) / (2 * a)
        raiz2 = (- b - math.sqrt(delta)) / (2 * a)
        print(f'As raizes são {raiz1} e {raiz2}')

"""
26 Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro 
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
a tabela abaixo:
CONSUMO  -  (Km/l) - MENSAGEM
menor que -  8    - Venda o carro!
entre     - 8 e 14 - Econômico!
maior que -  14   - Super econômico!
"""
km = float(input('Digite a distancia em quilometros: '))
l = float(input('Digite a quantidade de litros: '))

consumo = km / l

if consumo < 8:
    print('Venda o carro!')
elif 8 <= consumo <= 14:
    print('Econômico!')
else:
    print('Super econômico!')

"""
27 Escreva um programa que, dada a idade de um nadador, classifique-o em uma das 
seguintes categorias:
Categoria  -- idade
Infantil A  - 5 a 7
Infantil B  - 8 a 10
Juvenil A  -  11 a 13
Juvenil B  -  14 a 17
Sênior    -   maiores de 18 anos
"""
idade = int(input('Digite a idade do nadador: '))

if 5 <= idade <= 7:
    print('Categoria : Infantil A')
elif 8 <= idade <= 10:
    print('Categoria: Infatil B')
elif 11 <= idade <= 13:
    print('Categopria: Juvenil A')
elif 14 <= idade <= 17:
    print('Categoria: Juvenil B')
elif idade < 5:
    print('Nasdador muito novo para classificar')
else:
    print('Sênior - Maior de 18 anos')

"""
28 Faça um programa que leia três números positivos e efetue o calcule de uma das 
seguintes médias de acordo com um valor numérico digitado pelo usuário?
a - Geométrica: raiz cubica (x * y * z)
b - Ponderada: (x + (2 * y) + (3 * z)) / 6
c - Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
d - Aritimética: (x + y +z) / 3
"""
x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))
z = float(input('Digite o valor de z: '))

form = input('Selegione uma das médias a ser calculada: '
              '\n a - Geométrica '
              '\n b - Ponderada '
              '\n c - Harmônica '
              '\n d - Aritimética '
             '\n media : ')

if form == 'a':
    mediag = (x * y * z) ** (1/3)
    print(f'O resultaqdo da media geométrica foi: {mediag}')
elif form == 'b':
    mediap = (x + (2 * y) + (3 * z)) / 6
    print(f'O resultado da media ponderada foi: {mediap}')
elif form == 'c':
    mediah = 1 / ((1 / x) + (1 / y) + (1 / z))
    print(f'O resultado da media harmônica foi: {mediah}')
elif form == 'd':
    mediaa = (x + y +z) / 3
    print(f'O resultado da media aritimética foi: {mediaa}')
else:
    print('Não pertence há medias para ser calculadas')

"""
29 Faça uma prova matemática para crianças que estão aprendendo a somar números
interiores menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na 
tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a 
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas as perguntas e 
as respostas corretas, além de quantas vezes o aluno acertou.
"""
from random import randint

num1 = randint(1, 100)
num2 = randint(1, 100)

print(f'Qual é a soma de {num1} + {num2}?')
result1 = int(input(""))


num3 = randint(1, 100)
num4 = randint(1, 100)

print(f'Qual é a soma de {num3} + {num4}?')
result2 = int(input(""))


num5 = randint(1, 100)
num6 = randint(1, 100)

print(f'Qual é a soma de {num5} + {num6}?')
result3 = int(input(""))


num7 = randint(1, 100)
num8 = randint(1, 100)

print(f'Qual é a soma de {num7} + {num8}?')
result4 = int(input(""))


num9 = randint(1, 100)
num10 = randint(1, 100)

print(f'Qual é a soma de {num9} + {num10}?')
result5 = int(input(""))

acertos = 0
print()
if result1 == (num1 + num2):
    acertos += 1

if result2 == (num3 + num4):
    acertos += 1

if result3 == (num5 + num6):
    acertos += 1

if result4 == (num7 + num8):
    acertos += 1

if result5 == (num9 + num10):
    acertos += 1

print('Respostas:')
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num3} + {num4} = {num3 + num4}')
print(f'{num5} + {num6} = {num5 + num6}')
print(f'{num7} + {num8} = {num7 + num8}')
print(f'{num9} + {num10} = {num9 + num10}')
print()

print(f'Quantidade de acertos: {acertos}')

"""
30 Faça um programa que receba três números e mostre-os em ordem crescente
"""
x = int(input('Valor de x: '))
y = int(input('Valor de y: '))
z = int(input('Valor de z: '))

if (x >= y) and (y >= z):
    print(f'{z}, {y}, {x}')
elif (x >= z) and (z >= y):
    print(f'{y}, {z} {x}')
elif (y >= x) and (x >= z):
    print(f'{z}, {x}, {y}')
elif (y >= z) and (z >= x):
    print(f'{x}, {z}, {y}')
elif (z >= x) and (x >= y):
    print(f'{y}, {x}, {z}')
elif (z >= y) and (y >= x):
    print(f'{x}, {y}, {z}')
else:
    print('Algo aconteceu, vamos revisar?')
