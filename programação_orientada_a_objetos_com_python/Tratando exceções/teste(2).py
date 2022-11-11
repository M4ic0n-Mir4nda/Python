try:
    a = int(input('Entre com um número: '))
    b = int(input('Entre com outro numero: '))
    c = (a/b)
except ZeroDivisionError:
    print('[ERRO] Segundo número não pode ser zero!')
except Exception:
    print('Algo errado aconteceu')
else:
    print(c)