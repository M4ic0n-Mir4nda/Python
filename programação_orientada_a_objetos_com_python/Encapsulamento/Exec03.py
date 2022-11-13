class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    
class ContaBancaria:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, deposito, senha):
        if senha != self.cliente.get_senha():
            print('Senha incorreta')
        else:
            self.__saldo += deposito

    def sacar(self, saque, senha):
        if senha != self.cliente.get_senha():
            print('Senha incorreta')
        elif saque > self.__saldo:
            print('Saldo insufiente')
        else:
            self.__saldo -= saque


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

print(conta.get_saldo())            # Imprime 0
conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150
