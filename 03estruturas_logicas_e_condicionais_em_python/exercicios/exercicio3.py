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


