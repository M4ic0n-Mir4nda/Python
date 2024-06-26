"""Calculadora feature tests."""

from pytest import fixture
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from app.calculadora import soma

@fixture
def contexto():
    return {'num1': 0, 'num2': 0, 'resultado': 0}

@scenario('../features/calculadora.feature', 'Soma dois numeros')
def test_soma_dois_numeros():
    """Soma dois numeros."""

@given('eu tambem tenho o numero 7 como entrada para a calculadora')
def eu_tambem_tenho_o_numero_7_como_entrada_para_a_calculadora(contexto):
    """Eu tambem tenho o numero 7 como entrada para a calculadora."""
    contexto['num2'] = 7

@given('eu tenho o numero 2 como entrada para a calculadora')
def eu_tenho_o_numero_2_como_entrada_para_a_calculadora(contexto):
    """Eu tenho o numero 2 como entrada para a calculadora."""
    contexto['num1'] = 2

@when('eu solicito que realize a soma')
def eu_solicito_que_realize_a_soma(contexto):
    """Eu solicito que realize a soma."""
    contexto['resultado'] = soma(contexto['num1'], contexto['num2'])

@then('o resultado deve ser 9')
def o_resultado_deve_ser_9(contexto):
    """O resultado deve ser 9."""
    assert contexto['resultado'] == 9
