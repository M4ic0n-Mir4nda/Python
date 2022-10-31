class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, item):
        self.itens.append(item)
        
    def desenfileirar(self):
        return self.itens.pop(0)

    def tamanho(self):
        return len(self.itens)

    def vazio(self):
        if len(self.itens) == 0:
            return True
        else:
            return False 

    def primeiro(self):
        if len(self.itens) > 0:
            return self.itens[0]

    def mostrar(self):
        for i in self.itens:
            print(i, end=' ')

fila = Fila()
fila.enfileirar(2)
fila.enfileirar(2)
fila.enfileirar(0)
fila.enfileirar(0)
fila.enfileirar(9)
fila.enfileirar(6)
fila.enfileirar(6)
print(fila.mostrar())
fila.enfileirar(5)
fila.enfileirar(1)
fila.desenfileirar()
fila.enfileirar(5)
fila.desenfileirar()
fila.enfileirar(7)
fila.enfileirar(3)
fila.enfileirar(2)
fila.desenfileirar()

print(fila.mostrar())
    