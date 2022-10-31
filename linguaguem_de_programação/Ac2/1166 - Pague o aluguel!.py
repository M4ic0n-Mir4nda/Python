valor = int(input())
pagamento = int(input())
qtd = 1
while valor > 0:
    print(f'pagamento: {qtd}')
    print(f'antes = {valor}')
    pago = valor - pagamento
    qtd += 1
    valor -= pagamento
    if valor <= 0:
        pago = 0
        print(f'depois = {pago}')
        print('-' * 5)
        break
    print(f'depois = {pago}')
    print('-' * 5)
