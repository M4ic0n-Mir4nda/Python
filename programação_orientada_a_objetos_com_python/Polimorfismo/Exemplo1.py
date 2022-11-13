'''
Na POO, o polimorfismo permite que objetos se comportem de acordo com a classe à qual pertencem, 
ou de acordo com uma superclasse mais genérica (o objeto se comporta de formas diferentes).
'''

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print("Animal Comendo")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def latir(self):
        print("O Cachorro está latindo")

cachorro = Cachorro("Rex", "Rottweiler")
cachorro.comer()    # Comportamento da classe Animal
cachorro.latir()    # Comportamento da classe Cachorro
