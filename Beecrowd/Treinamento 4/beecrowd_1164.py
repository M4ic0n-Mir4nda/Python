def numero_perfeito(numero):
    for i in range(num):
        qtd = 0
        n = int(input())
        if 1 <= n <= 10**8:
            for j in range(n + 1):
                if qtd == n:
                    print(f'{n} eh perfeito')
                    break
                elif qtd > n:
                    print(f'{n} nao eh perfeito')
                    break
                elif n == 1:
                    print(f'{n} nao eh perfeito')
                    break
                qtd += j

num = int(input())
if 1 <= num <= 20:
    numero_perfeito(num)