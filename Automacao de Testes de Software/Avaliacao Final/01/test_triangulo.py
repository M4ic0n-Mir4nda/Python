# test_triangulo.py
import pytest
from verifica_triangulo import verifica_triangulo

def test_triangulo_equilatero():
    assert verifica_triangulo(5, 5, 5) == 'Equilátero'

def test_triangulo_isosceles():
    assert verifica_triangulo(5, 5, 3) == 'Isósceles'
    assert verifica_triangulo(5, 3, 5) == 'Isósceles'
    assert verifica_triangulo(3, 5, 5) == 'Isósceles'

def test_triangulo_escaleno():
    assert verifica_triangulo(5, 4, 6) == 'Escaleno'

def test_nao_triangulo():
    assert verifica_triangulo(1, 2, 3) == 'Não é um triângulo!'
    assert verifica_triangulo(1, 10, 12) == 'Não é um triângulo!'
    assert verifica_triangulo(10, 1, 12) == 'Não é um triângulo!'
    assert verifica_triangulo(10, 12, 1) == 'Não é um triângulo!'

# Testes adicionais para cobrir mais casos
@pytest.mark.parametrize("a,b,c,expected", [
    (0, 0, 0, 'Não é um triângulo!'),  # Triângulo com lados de comprimento zero
    (-1, -1, -1, 'Não é um triângulo!'),  # Triângulo com lados de comprimento negativo
    (5, 5, 10, 'Não é um triângulo!'),  # A soma de dois lados é igual ao terceiro
    (5, 10, 5, 'Não é um triângulo!'),  # A soma de dois lados é igual ao terceiro
    (10, 5, 5, 'Não é um triângulo!'),  # A soma de dois lados é igual ao terceiro
])
def test_triangulo_parametrizado(a, b, c, expected):
    assert verifica_triangulo(a, b, c) == expected
