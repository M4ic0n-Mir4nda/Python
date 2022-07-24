x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p1 = (x2 - x1) ** 2
p2 = (y2 - y1) ** 2
distancia = (p1 + p2) ** (1/2)
print('{:.4f}'.format(distancia))
