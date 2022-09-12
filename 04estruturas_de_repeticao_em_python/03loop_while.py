"""
Loop While

Forma geral

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5


# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero += 1

# OBS: Em um loop while é importante que cuidemos do critério de parada.

# C ou Java

while(expressão){
    //execução
}

# do while (C ou Java)

do {

}while(expressão);


Precisamos ter cuidado com o loop infinito que o while pode proporcionar, lçembrando que há alguns tipos de software que utilizam dele, como jogos e robôs.
"""

# Exemplo 2

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
