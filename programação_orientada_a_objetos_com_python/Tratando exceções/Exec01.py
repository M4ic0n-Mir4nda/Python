try:
    x = int(input('Primeiro valor: '))
    y = int(input('Segundi valor: '))
    z = x / y
except ValueError:
    print('Digite um número!')
except ZeroDivisionError:
    print('Não é possivel divisão por zero')
except Exception:
    print('Ocorreu algum erro')
else:
    print(f'O resultado da divisão é {z}')