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

"""
24 
"""
