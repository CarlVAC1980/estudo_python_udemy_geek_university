""""
41 Faça um programa que leia o valor da hora de trabalho (em reais) e o número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adiciondo 10% sobre
o valor calculado.
"""
vht = float(input("Digite o valor de hora de trabalho (em reais): "))
ht = float(input("Digite o valor de horas trabalhadas no mês: "))

pm = vht * ht
pf = pm + (pm  * 0.10)

print(f'O valor a ser pago é de R$ {pf}')

"""
42 Receba o salário-base de um funcionário. Calcule a imprima o salário a receber, sabendo-se
que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base
"""
salario_base = float(input('Digite o valor do salário-base: '))

grat = salario_base * 0.05
impost = salario_base * 0.07
salario_final = (salario_base - impost) + grat

print(f'Salário-base: R$ {salario_base} \nValor do imposto a ser descontado (7%): R$ {impost} \nValor da gratificação (5%): R$ {grat} \nValor do salário final : R$ {salario_final}')

"""
43 Escreva um programa de ajuda para vendedores. A partir de um valor total lido, motre:
 - o total a pagar com desconto de 10% a vista;
 - o valor de cada parcela, no parcelamento de 3x sem juros;
 - a comissão do vendedor, no caso da venda ser feita a vista (5% sobre o valor com desconto);
 - a comissão do vendedos, no caso da venda ser parcelada (5% sobre o valor total);
"""
total = float(input('Digite o valor total doa venda: '))

avista = total * 0.90
vparcel = total / 3

comis_avista = avista * 0.05
comis_parcel = total * 0.05

print(f'Valor a vista, com desconto de 10%: R$ {avista} '
      f'\nValor da parcela, no parcelamento de 3x sem juros: R$ {vparcel} '
      f'\nCamissão a vista: R$ {comis_avista} '
      f'\nComissão parcelada: R$ {comis_parcel}')

"""
44 Receba a altura do degrau de uma escada e a altura que  o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deve subir para atingir 
seu objetivo.
"""
degrau = float(input('Digite o valor do degrau: '))
altura = float(input('Digite a altura a ser alcançada: '))

degraus = int(altura / degrau)

print(f'Os degraus necessarios para se chegar a altura {altura} é: {degraus} degraus')

"""
45 Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela 
ASCII para resolver o problema.
"""
for i in range(65, 91):
    c = chr(ord(chr(i)) + 32)
    print(f'{chr(i)}, {c}')

"""
46 Faça um programa que leia um número inteiro positivo de três digitos ( de 100 a 999).
Gere outro numero formado pelos digitos invertidos do número lido. Exemplo:
 - número lido = 123
 - número gerado = 321
"""
lido = input('Digite um número de três digitos (100 a 999): ')

print(lido[::-1])

"""
47 Leia um digito inteiro de 4 dígitos ( de 1000 a 9999) e imprima 1 dígito por linha.
"""
digito = input('Digite um número de quatro digitos (1000 a 9999): ')

for i in range(0, 4):
    print(digito[i])

"""
48 Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos
"""
entrada = int(input('Digite um valor a ser convertido: '))

horas  = entrada // 3600
seg_rest = entrada % 3600
minutos = seg_rest // 60
seg_final = seg_rest % 60

print(f'o tatol de segundos {entrada} dá  {horas}(horas):{minutos}(minuots):{seg_final}(segundos)')
