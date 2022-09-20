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
33 
"""
