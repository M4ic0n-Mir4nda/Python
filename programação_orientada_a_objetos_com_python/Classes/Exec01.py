class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas


livro = Livro('Senhor dos Anéis', 'Vulgo jão', 425)
print(livro.titulo)
print(livro.autor)
print(livro.quantidade_paginas)
