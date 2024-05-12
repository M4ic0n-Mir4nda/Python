from bhaskara import calcular_raizes
import pytest


def test_bhaskara_uma_raiz():
    assert calcular_raizes(1, 0, 0) == (1, 0)

def test_bhaskara_duas_raizes():
    assert calcular_raizes(1, -5, 6) == (2, 3, 2)

def test_bhaskara_zero_raizes():
    assert calcular_raizes(10, 10, 10) == 0

def test_bhaskara_uma_raiz_negativa():
    assert calcular_raizes(10, 20, 10) == (1, -1)

def test_bhaskara_nao_eh_equacao_segundo_grau():
    with pytest.raises(ZeroDivisionError):
        assert calcular_raizes(0, 0, 0) == 0 

def test_bhaskara_tipo_coeficiente_a_invalido():
    with pytest.raises(TypeError):
        calcular_raizes('0', 0, 0)

def test_bhaskara_tipo_coeficiente_b_invalido():
    with pytest.raises(TypeError):
        calcular_raizes(0, '0', 0)

def test_bhaskara_tipo_coeficiente_c_invalido():
    with pytest.raises(TypeError):
        calcular_raizes(0, 0, '0') 