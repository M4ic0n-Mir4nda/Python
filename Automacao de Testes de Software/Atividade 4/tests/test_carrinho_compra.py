"""Carrinho de compras feature tests."""
from pytest import fixture
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from src.CarrinhoCompra import CarrinhoCompras

@fixture
def carrinho():
    return CarrinhoCompras()

@scenario('../features/carrinho.feature', 'Adicionar itens ao carrinho')
def test_adicionar_itens_ao_carrinho():
    """Adicionar itens ao carrinho."""

@scenario('../features/carrinho.feature', 'Remover itens do carrinho')
def test_remover_itens_do_carrinho():
    """Remover itens do carrinho."""

@given('que tenho um carrinho de compras com o item "Camiseta" e preco R$ 29.99')
def adicionar_camiseta(carrinho):
    """que tenho um carrinho de compras com o item "Camiseta" e preco R$ 29.99."""
    carrinho.adicionar_item('Camiseta', 29.99)

@when('eu adiciono o item "Calca" com o preco R$ 49.99')
def adiciona_calca(carrinho):
    """eu adiciono o item "Calca" com o preco R$ 49.99."""
    carrinho.adicionar_item('Calca', 49.99)

@then('o total do carrinho de compras deve ser R$ 79.98')
def total_carrinho(carrinho):
    """o total do carrinho de compras deve ser R$ 79.98."""
    assert carrinho.total() == 79.98

@when('eu removo o item do carrinho')
def remove_item(carrinho):
    """eu removo o item do carrinho."""
    carrinho.remover_item()

@then('o carrinho de compras deve estar vazio')
def carrinho_vazio(carrinho):
    """o carrinho de compras deve estar vazio."""
    assert carrinho.esta_vazio()



