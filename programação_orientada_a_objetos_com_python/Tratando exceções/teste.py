try:
    a = int(input('Entre com um número: '))
    b = int(input('Entre com outro numero: '))
    print(a/b)
except ZeroDivisionError:
    print('[ERRO] Segundo número não pode ser zero!')
except ValueError:
    print('Digite um número!')
except Exception:
    print('Algo errado aconteceu')