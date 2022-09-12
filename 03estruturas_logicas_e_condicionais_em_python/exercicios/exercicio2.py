"""
11 Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algorismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com
a mensagem "Número inválido".
"""
x = int(input('Digite um número inteiro maior que zero: '))

if x < 0:
    print('Número inválido')
else:
    soma = 0
    y = str(x)
    for i in range(len(y)):
        soma += int(y[i])
    print(soma)

"""
12 Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número 
inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""
import math

x = int(input('Digite um número inteiro: '))

if x < 0:
    print('Número inválido')
else:
    print(math.log(x))


"""
13 Faça um algoritmo que calcule a média ponderada das notas de 3 provas.A primeira e 
a segunda prova tem peso 1 e a terceira tem peso 2. Ao mostre a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""
x = float(input('Digite a nota da primeira prova: '))
y = float(input('Digite a nota da segunda prova: '))
z = float(input('Digite a nota da terceira prova: '))

media = ((x * 1) + (y * 1) + (z * 2)) / (1 + 1 +2)

if media < 60:
    print(f'A média do aluno é {media}, aluno reprovado')
else:
    print(f'A média do aluno é {media}, aluno aprovado')


"""
14 A nota final de um estudante é calculada a partir de três notas atribuidas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo 
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9), de
recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessarias.
"""

x = float(input('Digite a nota do Trabalho de Laboratório: '))
y = float(input('Digite a nota da Avaliação Semestral: '))
z = float(input('Digite a nota do Exame Final: '))

media = ((x * 2) + (y * 3) + (z * 5)) / (2 + 3 + 5)

if media <= 2.9:
    print(f'A média do aluno é {media}, aluno REPROVADO')
elif 3 <= media <= 4.9:
    print(f'A média do aluno é {media}, aluno em RECUPERAÇÂO')
else:
    print(f'A média do aluno é {media}, aluno APROVADO')

"""
15 Usando o switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia 
da semana correspondente a este número, iste é, domingo se 1, segunda se 2, e
assim por diante.
"""
dia = int(input('Digite o número referente ao dia: '))

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-Feira')
    case 3:
        print('Terça-Feira')
    case 4:
        print('Quarta-Feira')
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta-Feira')
    case 7:
        print('Sábado')
    case _:
        print('Valor inválido')

"""
16 Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. 
"""
mes = int(input('Digite o número referente ao mês: '))

match mes:
    case 1:
        print('janeiro')
    case 2:
        print('fevereiro')
    case 3:
        print('março')
    case 4:
        print('abril')
    case 5:
        print('maio')
    case 6:
        print('junho')
    case 7:
        print('julho')
    case 8:
        print('agosto')
    case 9:
        print('setembro')
    case 10:
        print('outubro')
    case 11:
        print('novembro')
    case 12:
        print('dezembro')
    case _:
        print('Valor inválido')

"""
17 Faça um programa que calcule e mostre a área de um trapazeo. Sabe-se que:
a = ((basemaior + basemenor) * altura) / 2
Lembre-se que a base maior e a base menor devem ser números maiores que zero.
"""
bmr = float(input('Digite o valor da base maior: '))
bmn = float(input('Digite o valor da base menor: '))
alt = float(input('Digite o valor da altura: '))

if bmr < 0 or bmn < 0:
    print('Valor de uma das bases esta inválido')
elif bmr < bmn:
    print('Valor da base maior é menor que o valor da base menor, revise!')
else:
    a = ((bmr + bmn) * alt) / 2
    print(f'A area do trapezeo é {a}')

"""
18 
"""
