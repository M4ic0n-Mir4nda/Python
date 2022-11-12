class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        return self.salario + (self.salario * (percentual / 100))


nome = input('Qual é o seu nome? ')
salario = input('E qual é o seu salário altualmente? ')
funcionario = Funcionario(nome, float(salario))
aumento = input('Qual é o percentual que você gostaria de receber no seu aumento? OBS: Digite um valor inteiro ')
print(f'Como você recebeu um aumento, o seu salário agora é R${funcionario.aumentar_salario(int(aumento)):.2f}')
