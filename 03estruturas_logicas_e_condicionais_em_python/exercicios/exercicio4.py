"""
31 Faça um programa que receba altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa

Altura                                       Peso
                        até 60       entre 60 e 90(inclusive)       acima de 90
menor que 1.210           A                   D                          G
de 1.20 a 1.70            B                   E                          H
Maior que 1.70            C                   F                          I

"""
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

if (altura < 1.20) and (peso <= 60.00):
    print('Sua classificação é: A')
elif (altura < 1.20) and (60.00 < peso <= 90.00):
    print('Sua classificação é: D')
elif (altura < 1.20) and (peso > 90.00):
    print('Sua classificação é: G')
elif (1.20 <= altura <= 1.70) and (peso <= 60):
    print('Sua classificação é: B')
elif (1.20 <= altura <= 1.70) and (60.00 < peso <= 90.00):
    print('Sua classificação é: E')
elif (1.20 <= altura <= 1.70) and (peso > 90.00):
    print('Sua classificação é: H')
elif (altura > 1.70) and (peso <= 60):
    print('Sua classificação é: C')
elif (altura > 1.70) and (60.00 < peso <= 90.00):
    print('Sua classificação é: F')
elif (altura > 1.70) and (peso > 90.00):
    print('Sua classificação é: I')
else:
    print('Algo deu errado')

"""
32 Escreva um programa que leia o código do produto escolhido no cardapio de uma lanchonete
e a quantidade. O programa deve calcular o valor sa ser pago por aquele lanche. Considere
que a cada execução somente será calculado um pedido. O cardapio da lanchonete segue o padrão abaixo:
Especificação      |  Código    |     Preço
Cachorro Quente    |    100     |     1.20  
Bauru Simples      |    101     |     1.30  
Bauru com Ovo      |    102     |     1.50  
Hamburguer         |    103     |     1.20   
Cheeseburguer      |    104     |     1.70
Suco               |    105     |     2.20   
Refrigerante       |    106     |     1.00
"""
cod = int(input('Digite o codigo do produto: '))
x = int(input('Digite a quantidade do produto'))

if cod == 100:
    print(f'Total a ser pago: {1.2 * x}')
elif cod == 101:
    print(f'Total a ser pago: {1.3 * x}')
elif cod == 102:
    print(f'Total a ser pago: {1.5 * x}')
elif cod == 103:
    print(f'Total a ser pago: {1.2 * x}')
elif cod == 104:
    print(f'Total a ser pago: {1.7 * x}')
elif cod == 105:
    print(f'Total a ser pago: {2.2 * x}')
elif cod == 106:
    print(f'Total a ser pago: {1.3 * x}')
else:
    print('Código inválido!')

"""
33 Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo e escreva uma mensagem em função do novo preço ( de
acordo com a segunda tabela).
|  Preço Antigo    |   Percentual   |   
| até R$ 50.00     |        5%      |
| entre R$ 50 e 100|        10%     |
| acima de R$ 100  |        15%     | 

|    Preço Novo       |     Mensagem  |
| até R$  80          |     Barato    |
|entre 80 e 120(incl) |     Normal    |
|entre 120 e 200(incl)|     Caro      |
|acima de 200         |   Muito caro  |
"""
preco = float(input('Digite o preço antigo: '))
preco_novo = 0
if preco < 50:
    preco_novo = preco + (preco * 0.05)
    print(f'O novo preço é R$ {preco_novo}')
elif 50 <= preco <= 100:
    preco_novo = preco + (preco * 0.10)
    print(f'O novo preço é R$ {preco_novo}')
elif preco > 100:
    preco_novo = preco + (preco * 0.15)
    print(f'O novo preço é R$ {preco_novo}')

if preco_novo < 80:
    print('Barato!')
elif 80 <= preco_novo <= 120:
    print('Normal')
elif 120 < preco_novo <= 200:
    print('Caro')
elif preco_novo > 200:
    print('Muito Caro')

"""
34 Leia a nota e o npúmero de faltas de um aluno, e escreva seu conceito. De acordo com a 
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

|    Nota    |    Conceito(até 20 faltas)    |    Conceito(mais de 20 faltas)    |
|9.0 até 10.0|               A               |                  B                |
|7.5 até 8.9 |               B               |                  C                |
|5.0 até 7.4 |               C               |                  D                |
|4.0 até 4.9 |               D               |                  E                |
|0.0 até 3.9 |               E               |                  E                |
"""
nota = float(input('Digite a nota: '))
faltas = int(input('Digite a quantidade de faltas: '))

if 9.0 >= nota <= 10.0:
    if faltas <= 20:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito A')
    else:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito B')
elif 7.5 >= nota <= 8.9:
    if faltas <= 20:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito B')
    else:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito C')
elif 5.0 >= nota <= 7.4:
    if faltas <= 20:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito C')
    else:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito D')
elif 4.0 >= nota <= 4.9:
    if faltas <= 20:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito D')
    else:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito E')
elif 0.0 >= nota <= 3.9:
    if faltas <= 20:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito E')
    else:
        print(f'Nota: {nota} - Faltas: {faltas} - Conteito E')
else:
    print('Nota inválida')

"""
35 Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, 
e se o dia existe naquele mês. Note que Fevereiro tem 29 em ano bisextos, e 28 dias em anos não bisextos.
"""

d = int(input('Digite o dia: '))
m = int(input('Digite o mês: '))
a = int(input('Digite o ano: '))

if a != 0:
    if m == 1:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 2:
        if (a % 400 == 0) or ((a % 4 == 0) and not (a % 100 == 0)):
            if (d >= 1) and (d <= 29):
                print('Data válida, ano bisexto!')
            else:
                print('Data inválida!')
        else:
            if (d >= 1) and (d <= 28):
                print('Data válida!')
            else:
                print('Data inválida!')
    elif m == 3:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 4:
        if (d >= 1) and (d <= 30):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 5:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 6:
        if (d >= 1) and (d <= 30):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 7:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 8:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 9:
        if (d >= 1) and (d <= 30):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 10:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 11:
        if (d >= 1) and (d <= 30):
            print('Data válida!')
        else:
            print('Data inválida!')
    elif m == 12:
        if (d >= 1) and (d <= 31):
            print('Data válida!')
        else:
            print('Data inválida!')
    else:
        print('Mês inexistente!')
else:
    print('Aconteceu algo de errado')