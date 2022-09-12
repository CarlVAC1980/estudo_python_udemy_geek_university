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

