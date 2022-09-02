"""
Recebendo dados de usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
 - Aspas simpes;
 - Aspas duplas;
 - Aspas simples Triplas;
 - Aspas duplas triplas;

"""
# Entrada de dados
# print("Qual seu nome?")
# nome = input()

nome = input('Qual seu nome? ')

# Exemplo de print antigo 2.x
# print ('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo atual de print 3.7
print(f'Seja bem-vind(a) {nome}')

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print antigo 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print moderno 3.x
# print('O(A) {0} tem {1} anos'.format(nome, idade))

# Exemplo atual de print 3.7
print(f'O(A) {nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'O(A) {nome} nasceu em {2022 - int(idade)}')
