from abc import ABC # Devemos importar a classe ABC do módulo abc (abstract base classes)

 # A classe abstrata deve herdar da classe ABC

class Pessoa(ABC): 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

class Aluno(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina


funcionario = Funcionario('João', 25, 1500.0)   # Somente as classes 
aluno = Aluno('Pedro', 19, 'Programação')       # filhas devem ser instanciadas