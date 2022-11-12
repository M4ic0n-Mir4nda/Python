def converte_para_celsius(fahrenheit):
    celsius = (5.0/9.0) * (fahrenheit - 32)
    return celsius


def converte_para_fahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit


try:
    assert converte_para_celsius(32) == 0
    print('Está correto')
except AssertionError:
    print('Está incorreto')

try:
    assert converte_para_celsius(41) == 5.0
    print('Está correto')
except AssertionError:
    print('Está incorreto')

try:
    assert converte_para_fahrenheit(0) == 32
    print('Está correto')
except AssertionError:
    print('Incorreto')

try:
    assert converte_para_fahrenheit(27) == 80.6
    print('Está correto')
except AssertionError:
    print('Incorreto')