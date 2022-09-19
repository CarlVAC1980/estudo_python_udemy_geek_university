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
32 
"""
