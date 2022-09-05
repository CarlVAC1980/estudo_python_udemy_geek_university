"""
Tipo String

Em Python um dado é considerado um tipo String quando:

 - Estiver em aspas simples -> 'uma string', '234', 'a', 'True', '4.32'
 - Estiver em aspas duplas -> "uma string", "234", "a", "True", "4.32"
 - Estiver em aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''4.32'''
"""
#Estiver em aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """4.32"""
"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de Strings

print(nome[0:4]) # Slice de String

print(nome[5:15]) # Slice de String

print(nome.split()[0])

print(nome.split()[1])
"""

nome = 'Geek University'
# [::-1] Comece do primeiro elemento, vá até o ultimo elemento e inverta
print(nome[::-1]) # Inversão da String Pythonico

print(nome.replace('e', 'i'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palindromo
print(texto)

print(texto[::-1])
