def triangulo_alfabetico(n):
    qtd = 0
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    if 1 <= n <= 26:
        for i in range(1, n + 1):
            for j in range(i):
                if qtd == n:
                    qtd -= 1
                print(alfabeto[qtd], end='')
            qtd += 1
            print()
        return n
x = int(input())
triangulo_alfabetico(x)
