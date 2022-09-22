# ARQUIVO DE TESTE
# Este é um programa de teste para a Atividade Continua 01.
# Este arquivo não deve ser alterado.

from ac01 import pertence, substituir, posicoes, reprovados, excluir_nota, menor_nota


# --------------------------------------------------------------
try:
    lista = [2, 3, 4, 8, 7]
    resultado = pertence(lista, 3, 8, 2)
    assert resultado == 1
    print('pertence - CORRETO')
except AssertionError:
    print('pertence - ERRADO')

try:
    lista = [2, 0, 4, 8, 7]
    resultado = pertence(lista, 8, 0, 7)
    assert resultado == 1
    print('pertence - CORRETO')
except AssertionError:
    print('pertence - ERRADO')

try:
    lista = [2, 3, 4, 8, 7]
    resultado = pertence(lista, 3, 8, 9)
    assert resultado == 0
    print('pertence - CORRETO')
except AssertionError:
    print('pertence - ERRADO')

try:
    lista = [2, 3, 4, 8, 7, 50, 2]
    resultado = pertence(lista, 5, 9, 1)
    assert resultado == 0
    print('pertence - CORRETO')
except AssertionError:
    print('pertence - ERRADO')


# --------------------------------------------------------------
try:
    lista = (1, 2, 3, 2, 4, 2, 2, 22, 1, 8)
    resultado = substituir(lista, 2, 99)
    assert resultado == (1, 99, 3, 99, 4, 99, 99, 22, 1, 8)
    print('substituir - CORRETO')
except AssertionError:
    print('substituir - ERRADO')

try:
    lista = (1, 2, 2, 4)
    resultado = substituir(lista, 2, 'abc')
    assert resultado == (1, 'abc', 'abc', 4)
    print('substituir - CORRETO')
except AssertionError:
    print('substituir - ERRADO')

try:
    lista = (1, 2, 2, 4)
    resultado = substituir(lista, 3, 9)
    assert resultado == (1, 2, 2, 4)
    print('substituir - CORRETO')
except AssertionError:
    print('substituir - ERRADO')


# --------------------------------------------------------------
try:
    tupla = (1, 2, 3, 4, 5)
    resultado = posicoes(tupla, 2)
    assert resultado == [1]
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')

try:
    tupla = (2, 1, 2, 3, 2, 2, 9, 2)
    resultado = posicoes(tupla, 2)
    assert resultado == [0, 2, 4, 5, 7]
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')

try:
    tupla = (2, 1, 2, 3, 2)
    resultado = posicoes(tupla, 5)
    assert resultado == []
    print('posicoes - CORRETO')
except AssertionError:
    print('posicoes - ERRADO')


# --------------------------------------------------------------
try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = reprovados(alunos)
    assert resultado == ['Ana Paula', 'Augusto']
    print('reprovados - CORRETO')
except AssertionError:
    print('reprovados - ERRADO')

try:
    alunos = {'Augusto': [10, 8.0, 7.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [8.0, 9.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = reprovados(alunos)
    assert resultado == []
    print('reprovados - CORRETO')
except AssertionError:
    print('reprovados - ERRADO')


# --------------------------------------------------------------
try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5, 9.0],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_nota(alunos, 'Denise', 9.0)
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    print('excuir_nota - CORRETO')
except AssertionError:
    print('excuir_nota - ERRADO')

try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_nota(alunos, 'Marcelo', 7.0)
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0, 8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0]}
    print('excuir_nota - CORRETO')
except AssertionError:
    print('excuir_nota - ERRADO')

try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_nota(alunos, 'Denise', 7.0)
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0, 8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    print('excuir_nota - CORRETO')
except AssertionError:
    print('excuir_nota - ERRADO')

try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = excluir_nota(alunos, 'João', 10)
    assert resultado == {'Augusto': [4.5, 7.0, 6.0, 3.0],
                         'Denise': [9.0, 8.5],
                         'Ana Paula': [3.5, 1.0, 6.5],
                         'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    print('excuir_nota - CORRETO')
except AssertionError:
    print('excuir_nota - ERRADO')


# --------------------------------------------------------------
try:
    alunos = {'Augusto': [4.5, 7.0, 6.0, 3.0],
              'Denise': [9.0, 8.5],
              'Ana Paula': [3.5, 1.0, 6.5],
              'Marcelo': [9.0, 10.0, 7.0, 7.0]}
    resultado = menor_nota(alunos)
    assert resultado == {'Augusto': 3.0,
                         'Denise': 8.5,
                         'Ana Paula': 1.0,
                         'Marcelo': 7.0}
    print('menor_nota - CORRETO')
except AssertionError:
    print('menor_nota - ERRADO')


# --------------------------------------------------------------