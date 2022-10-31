inicio = int(input())
fim = int(input())
qtd = 0
if 0 <= inicio <= fim <= 9999:
    for i in range(inicio, fim + 1):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            print(i)
            qtd += 1
print(f'bissextos: {qtd}')
