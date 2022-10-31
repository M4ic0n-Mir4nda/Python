mercadoria = float(input())
qtde = int(input())
preco = qtde * mercadoria
percentual = qtde * 1.0 / 100.0
desc_fixo = (0.90 - percentual) * preco
print(f'{preco:.2f}')
print(f'{desc_fixo:.2f}')
