"""
Estruturas logicas: and (e), or (ou), not (não), is (é)

Operadors unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:

Para o 'and' ambos os valores precisam ser True
 - if ativo and logado:
Para o 'or' um ou outro precisa ser True
 - if ativo or logado:
Para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True
 - if not ativo:
Para o 'is', o valor é comparado com o segundo.
 - print(ativo is False)
"""
ativo = True
logado = True

if not ativo:
    print('Bem-vindo usuário!')
else:
    print('Você precisa ativar a sua conta. Pro favor cheque seu e-mail')

# ativo é falso?
print(ativo is False)
