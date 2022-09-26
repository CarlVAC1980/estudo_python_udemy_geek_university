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


"""
36) Escreva um programa que, dado o valor da venda, imprima a comissão
que deverá ser paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

    | Venda mensal                                            | Comissão
    | Maior ou igual a R$100.000,00                           | R$700,00 + 16% das vendas
    | Menor que R$100.000,00 e maior ou igual a R$80.000,00   | R$650,00 + 14% das vendas
    | Menor que R$80.000,00 e maior ou igual a R$60.000,00    | R$600,00 + 14% das vendas
    | Menor que R$60.000,00 e maior ou igual a R$40.000,00    | R$550,00 + 14% das vendas
    | Menor que R$40.000,00 e maior ou igual a R&20.000,00    | R$500,00 + 14% das vendas
    | Menor que R$20.000,00                                   | R$400,00 + 14% das vendas
"""

venda = float(input('Digite o valor da venda: '))

if venda >= 100000:
    comissao = 700 + (venda * 0.16)
    print(f'Comissão é de : R$ {comissao:.2f}')
elif 80000 <= venda < 100000:
    comissao = 650 + (venda * 0.14)
    print(f'Comissão é de : R$ {comissao:.2f}')
elif 60000 <= venda < 80000:
    comissao = 600 + (venda * 0.14)
    print(f'Comissão é de : R$ {comissao:.2f}')
elif 40000 <= venda < 60000:
    comissao = 550 + (venda * 0.14)
    print(f'Comissão é de : R$ {comissao:.2f}')
elif 20000 <= venda < 40000:
    comissao = 500 + (venda * 0.14)
    print(f'Comissão é de : R$ {comissao:.2f}')
elif venda < 20000:
    comissao = 400 + (venda * 0.14)
    print(f'Comissão é de : R$ {comissao:.2f}')
else:
    print('Valor inválido')

"""
37) As tarifas de certo parque de estacionamento são as seguintes:
    - 1ª e 2ª hora - R$1,00 cada
    - 3ª e 4ª hora - R$1,40 cada
    - 5ª hora e seguintes - R$2,00 cada
O número de horas a pagar é sempre inteiro e arredondado por execesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida deste
sao apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12,50 representará 'dez para a uma da parte'. Pretende-se
criar um programa que, lidos pelo teclado os momentos de chegada e de partida, escreva
na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida
se dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada
for supeiror à da partida, isso não é uma situação de erro, antes siginificará que
a partida ocorreu no dia seguinte ao chegada.
"""
h_chegada = int(input('Digite a hora da chegada: '))
m_chegada = int(input('Digite o minuto de chegada: '))

h_saida = int(input('Digite a hora de saida: '))
m_saida = int(input('Digite o minuto de saida: '))

total_horas = 0

# Validando as horas
if 0<= h_chegada < 24 and 0 <= h_saida < 24:
    if 0 <= m_chegada < 60  and 0 <= m_saida < 60:
        # Arredondando horas, por minutos a mais
        if h_saida == h_chegada and m_saida > m_chegada:
            total_horas += 1

        # Arredondando dia, 23:01 ou mais
        elif h_saida == h_chegada and m_saida < m_chegada:
            total_horas = 24

        elif h_saida > h_chegada:
            total_horas = h_saida - h_chegada

            if m_chegada >= m_saida:
                pass
            else:
                total_horas += 1

        else:
            total_horas = 24 - (h_chegada - h_saida)

            if m_chegada >= m_saida:
                pass
            else:
                total_horas += 1
    else:
        print('Minutos fora do intervalo 00 à 59.')

else:
    print('Hota fora do intervalo de 00 à 23')

if total_horas > 0:
    print(f'Tempo de permanencia: {total_horas}hs')

    if 1 <= total_horas <= 2:
        print(f'Total a pagar R$ {total_horas * 1.00}')
    elif 3 <= total_horas <= 4:
        print(f'Total a pagar R$ {total_horas * 1.40}')
    elif total_horas > 5:
        print(f'Total a pagar R$ {total_horas * 2.00}')
    else:
        print('Erro')


"""
38) Leia uma data de nascimento de uma pessoa fornecida através de três números
inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma
data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês
(29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro,
dia <= 31 nos outros meses. Teste a validade do mês: mês > 0 e mês <13. Teste a
validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008).
Imprimir: "data válida" ou "data inválida" no final da execução.
"""
d = int(input('Digite o dia: '))
m = int(input('Digite o mês: '))
a = int(input('Digite o ano: '))


anot_atual = 2008

if a <= anot_atual:
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
        print('Data inválida!')
else:
    print('Data inválida!')



"""
39) Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que consideraa o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.
    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |

"""
salario_atual = float(input('Digite o valor do salário atual: '))
tempo_servico = int(input('Digite o tempo de serviço em anos: '))
reajuste = 0
if salario_atual <= 500:
    reajuste = salario_atual + (salario_atual * 0.25)
elif 500 < salario_atual <= 1000:
    reajuste = salario_atual + (salario_atual * 0.20)
elif 1000 < salario_atual <= 1500:
    reajuste = salario_atual + (salario_atual * 0.15)
elif 1500 < salario_atual <= 2000:
    reajuste = salario_atual + (salario_atual * 0.10)
else:
    print('Sem reajuste!')

bonus = 0
if tempo_servico < 1:
    print('Sem bonus!')
elif 1 <= tempo_servico <= 3:
    bonus = 100
elif 4 <= tempo_servico <= 6:
    bonus = 200
elif 7 <= tempo_servico <= 10:
    bonus = 300
else:
    bonus = 500

print(f'Você recebe atualmente {salario_atual}, tem {tempo_servico} de tempo de serviço e ganhará um reajuste no valor de {reajuste} mais um bônus de {bonus} por tempo de serviço, dando um total de {reajuste + bonus}')