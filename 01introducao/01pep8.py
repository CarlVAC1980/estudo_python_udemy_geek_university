"""
PEP 8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythonica

[1] - Utilize Camel Case para nomes de classes:

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minusculo, separados por underline para funções ou variáveis:

def soma():
    pass

def soma_dois():
    pass

[3] - Utilize 4 espaços para identação!

if 'a' in bannana:
    print('tem')

[4] - Linhas em branco:
- Separar funções e definições de classe com duas linhas em branco:
- Médotos dentro de uma classe devem ser separados com uma única linha em branco:

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas:

# Import Errado

import sys, os

# Import CErto

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote , recomenda-se fazer:

from types import (
    StringType,
    ListType
    SetType,
    OutroType
)

# Imports devem ficar no topo do arquivo

[6] - Espaços em expressões e instruções

# Não faça

funcao(_algo[_1_], {_outro: 2_}_)

# Faça

funcao(algo[1], {òutro: 2})

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
