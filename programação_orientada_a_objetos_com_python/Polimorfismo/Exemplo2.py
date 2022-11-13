# O Polimorfismo também ocorre quando uma subclasse sobrescreve algum método herdado da superclasse.

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print("Animal Comendo")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def comer(self):
        print("Cachorro", self.nome, "Comendo") # Método comer foi sobrescrito na classe-filha


cachorro = Cachorro("Rex", "Rottweiler")
cachorro.comer()                # executa o método sobrescrito