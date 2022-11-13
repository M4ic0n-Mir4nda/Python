from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.10)


gerente = Gerente('Joao', 123, 2000.0)
assistente = Assistente('Larissa', 456, 1100.0)
vendedor = Vendedor('Maicon', 789, 1600.0)

print(gerente.calcular_salario())
print(assistente.calcular_salario())
print(vendedor.calcular_salario())
