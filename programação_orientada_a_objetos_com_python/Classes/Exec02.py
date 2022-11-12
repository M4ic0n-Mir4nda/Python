class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c


a = 1
b = 2
c = 3
triangulo = Triangulo(a, b, c)
print(triangulo.calcular_perimetro())
