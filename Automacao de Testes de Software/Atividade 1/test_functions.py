from functions import calcula_salario_liquido, calcula_desconto, calcula_desconto_reais, calcula_gorjeta

def test_calcula_salario_liquido():
    assert calcula_salario_liquido(6.25, 160, 1.3) == (987.0)
    assert calcula_salario_liquido(20.5, 240, 1.7) == (4836.36)
    assert calcula_salario_liquido(13.9, 200, 6.48) == (2599.86)

def test_calcula_desconto():
    assert calcula_desconto(100) == (91.0, 9.0)
    assert calcula_desconto(1500) == (1365.0, 135.0)
    assert calcula_desconto(60000) == (54600.0, 5400.0)

def test_calcula_desconto_reais():
    assert calcula_desconto_reais(500.0, 50.0) == (450.0)
    assert calcula_desconto_reais(10500.0, 500.0) == (10000.0)
    assert calcula_desconto_reais(90.0, 0.80) == (89.20)

def test_calcula_gorjeta():
    assert calcula_gorjeta(75.0) == (82.50, 7.5)
    assert calcula_gorjeta(125) == (137.50, 12.5)
    assert calcula_gorjeta(350.87) == (385.96, 35.09)