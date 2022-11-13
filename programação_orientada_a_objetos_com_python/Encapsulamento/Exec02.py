class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


filmes = []
for i in range(3):
    titulo = (input('Qual é o titulo do filme? '))
    genero = (input('E o genero? '))
    filme = Filme(titulo, genero)
    filmes.append(filme)

for filme in filmes:
    print(f'Filme: {filme.get_titulo()}')
    print(f'Genero: {filme.get_genero()}')
    