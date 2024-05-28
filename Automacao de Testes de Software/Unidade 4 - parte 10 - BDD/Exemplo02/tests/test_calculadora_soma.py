"""features/calculadora.feature feature tests."""
from pytest import fixture

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)

from src.calculadora import soma

@fixture
def contexto():
    return {'num1': 0, 'num2': 0, 'resultado': 0}

@scenario('../features/calculadora.feature', 'Soma dois numeros')
def test_soma_dois_numeros():
    """Soma dois numeros."""

# Como se pode observar pela Figura 10.6, existem várias alterações realizadas para o tratamento de números inteiros. Cada parâmetro delimitado por < e > nas cláusulas @given, @when e @then foram alteradas. Por exemplo, o parâmetro <num1> foi substituído por {num1:d}. Isto significa que o parâmetro num1 é do tipo inteiro (d).  Note que para o pytest entender que o parâmetro num1 é do tipo inteiro, ele é preciso ser traduzido. Para isso, é necessário utilizar a instrução parser.parser(), do pacote pytest_bdd.

# E por fim, a fixture contexto e os parâmetros são transmitidos como parâmetros formais nas funções de testes. 
@given(parsers.parse('Eu entro um numero {num1:d} na calculadora'))
def eu_entro_um_numero_num1_na_calculadora(contexto, num1):
    """Eu entro um numero <num1> na calculadora."""
    contexto['num1'] = num1


@given(parsers.parse('Eu tambem entro com o valor {num2:d} na calculadora'))
def eu_tambem_entro_com_o_valor_num2_na_calculadora(contexto, num2):
    """Eu tambem entro com o valor <num2> na calculadora."""
    contexto['num2'] = num2


@when(parsers.parse('Eu solicito para realizar a soma.'))
def eu_solicito_para_realizar_a_soma(contexto):
    """Eu solicito para realizar a soma.."""
    contexto['resultado'] = soma(contexto['num1'], contexto['num2'])


@then(parsers.parse('Entao a soma deve ser {resultado:d}'))
def entao_a_soma_deve_ser_resultado(contexto, resultado):
    """Entao a soma deve ser <resultado>."""
    assert contexto['resultado'] == resultado