class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop()

    def tamanho(self):
        return len(self.itens)

    def vazia(self):
        if len(self.itens) == 0:
            return True
        else:
            return False

    def topo(self):
        if len(self.itens) > 0:
            return self.itens(-1)

    def mostrar(self):
        for i in self.itens:
            print(i, end=' ')

pilha = Pilha()
pilha.empilhar(2)
pilha.empilhar(2)
pilha.empilhar(0)
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(6)
pilha.empilhar(8)
pilha.desempilhar()
pilha.desempilhar()
pilha.desempilhar()
pilha.empilhar(5)
pilha.empilhar(7)
pilha.empilhar(3)
pilha.desempilhar()
pilha.desempilhar()


print(pilha.mostrar())