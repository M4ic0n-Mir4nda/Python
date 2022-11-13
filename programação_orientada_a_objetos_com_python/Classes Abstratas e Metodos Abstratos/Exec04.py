from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero_conta, nome, saldo):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    @abstractmethod
    def deposito(self, deposito):
        pass

    @abstractmethod
    def saque(self, saque):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero_conta, nome, saldo):
        super().__init__(numero_conta, nome, saldo)

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= saque

    def consultar_saldo(self):
        print(f'Saldo: {self.saldo}')


class ContaPoupanca(Conta):
    def __init__(self, numero_conta, nome, saldo):
        super().__init__(numero_conta, nome, saldo)

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        if saque > self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= saque

    def consultar_saldo(self):
        print(f'Saldo: {self.saldo}')


class ContaCorrenteEspecial(Conta):
    def __init__(self, numero_conta, nome, saldo, limite):
        super().__init__(numero_conta, nome, saldo)
        self.limite = limite

    def deposito(self, deposito):
        self.saldo += deposito

    def saque(self, saque):
        if saque > self.limite + self.saldo:
            print('Saldo insuficiente')
        else:
            self.saldo -= saque

    def consultar_saldo(self):
        print(f'Saldo: {self.saldo}')


contacorrente = ContaCorrente(123, "Paulo", 100)
contacorrente.saque(200)
contacorrente.consultar_saldo()
print('----------------------------')

contaespecial = ContaCorrenteEspecial(555, "Paulo", 100, 300)
contaespecial.saque(200)
contaespecial.consultar_saldo()
print('----------------------------')

contapoupanca = ContaPoupanca(333, "João", 100)
contapoupanca.saque(200)
contapoupanca.consultar_saldo()