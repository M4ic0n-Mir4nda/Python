def soma(a, b):
    return a + b

try:
    assert soma(2, 3) == 6
    print('Correto')
except AssertionError:
    print('Incorreto')