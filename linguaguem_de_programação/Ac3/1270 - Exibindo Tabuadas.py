def tabuada(n1, n2):
    for numero in range(n1, n2 + 1):
        for i in range(1, 10 + 1):
            print(f'{numero} x {i} = {numero * i}')
        print('-' * 10)

num1 = int(input())
num2 = int(input())
if num1 > num2:
    print('Nenhuma tabuada no intervalo!')
else:
    tabuada(num1, num2)