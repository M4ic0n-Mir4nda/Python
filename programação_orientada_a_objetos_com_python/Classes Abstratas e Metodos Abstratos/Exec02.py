from abc import ABC

class Veterinario():
    def examinar(self, animal):
        return animal.emitir_som()


class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cachorro(Animal):
    def emitir_som(self):
        print('Auau')


class Gato(Animal):
    def emitir_som(self):
        print('Miau')


class Cavalo(Animal):
    def emitir_som(self):
        print('CAVALO!')


dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

print('-' * 30)

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato
