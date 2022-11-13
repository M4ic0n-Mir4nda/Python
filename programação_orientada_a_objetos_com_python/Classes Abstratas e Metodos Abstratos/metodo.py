from abc import ABC, abstractmethod             # Devemos importar a classe abstractmethod do módulo abc

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod                             # Para definir o método abstrato utiliza-se a instrução @abstractmethod antes da definição do método                                   
    def exibir_nome(self):                      # O método abstrato deve ser vazio (contém apenas um pass).
        return


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def exibir_nome(self):                      # Os métodos abstratos devem ser implementados, obrigatoriamente, em todas as classes filhas    
        print("Nome do Funcionario: ", self.nome)


class Aluno(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_nome(self):                      # Os métodos abstratos devem ser implementados, obrigatoriamente, em todas as classes filhas
        print("Nome do Aluno: ", self.nome)

funcionario = Funcionario("João", 25, 1500.0)
aluno = Aluno("Pedro", 19, "Programação")
print(aluno.exibir_nome())
print(funcionario.exibir_nome())
