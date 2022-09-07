"""
Estrutura de repetição Loop for

Loop  -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = ; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop



Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteráveis:
- String
    nome = 'Geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos de transformar em lista

#Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre range)
"""
range(valor_inicial, valor_final)

OBS: O valor final não incluso 
"""
for numero in range(1, 10):
    print(numero)
