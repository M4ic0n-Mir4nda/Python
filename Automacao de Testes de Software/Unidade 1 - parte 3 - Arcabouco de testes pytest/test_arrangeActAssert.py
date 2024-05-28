from bhaskara import calcular_raizes

def test_bhaskara_uma_raiz():
    # arrange
    a = 1
    b = 0
    c = 0
    valor_esperado = (1, 0)
    # act
    valor_obtido = calcular_raizes(a, b, c) 
    # assert
    assert valor_obtido == valor_esperado

def test_bhaskara_duas_raizes():
    # arrange
    a = 1
    b = -5
    c = 6
    valor_esperado = (2, 3, 2)
    # act
    valor_obtido = calcular_raizes(a, b, c) 
    # assert
    assert valor_obtido == valor_esperado

def test_bhaskara_zero_raizes():
    # arrange
    a = 10
    b = 10
    c = 10
    valor_esperado = 0
    # act
    valor_obtido = calcular_raizes(a, b, c)  
    # assert
    assert valor_obtido == valor_esperado