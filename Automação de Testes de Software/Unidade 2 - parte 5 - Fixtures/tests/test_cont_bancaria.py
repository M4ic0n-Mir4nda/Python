import pytest

def test_criar_conta_bancaria_devolve_numero_correto(conta):
    assert conta.numero == 1

def test_criar_conta_bancaria_devolve_saldo_zerado(conta):
    assert conta.get_saldo(senha='1234') == 0

def test_depositar_valor_em_conta_devolve_saldo_aumentado(conta):
    assert conta.get_saldo(senha='1234') == 0
    conta.depositar(100, '1234')
    assert conta.get_saldo(senha='1234') == 100

def test_sacar_valor_em_conta_bancaria_devolve_saldo_menor(conta):
    conta.depositar(100, '1234')
    assert conta.get_saldo(senha='1234') == 100
    conta.sacar(20, '1234')
    assert conta.get_saldo(senha='1234') == 80

@pytest.mark.parametrize("valor_deposito, valor_saque, valor_esperado",[
    (30, 10, 20),
    (20, 2, 18),
    (50, 25, 25),
    (15, 15, 0)
])
def test_transacao(conta, valor_deposito, valor_saque, valor_esperado):
    conta.depositar(valor_deposito, '1234')
    conta.sacar(valor_saque, '1234')
    conta.get_saldo(senha='1234') == valor_esperado
