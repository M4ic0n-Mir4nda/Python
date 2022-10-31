soma = 0
while True:
    vic_coin = 2.50
    valor = float(input())
    if valor >= 0:
        soma += valor
    else:
        break
print(f'VC$ {soma:.2f}')
print(f'R$ {soma * vic_coin:.2f}')