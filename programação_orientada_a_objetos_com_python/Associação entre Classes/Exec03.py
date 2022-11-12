class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade


class Medico:
    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao


class Exame:
    def __init__(self, medico, paciente, descricao, resultado):
        self.medico = medico
        self.paciente = paciente
        self.descricao = descricao
        self.resultado = resultado

    def imprimir_exame(self):
        print(f'Nome do médico: {self.medico.nome}')
        print(f'CRM: {self.medico.crm}')
        print(f'Especialização: {self.medico.especializacao}')
        print(f'Nome do paciente {self.paciente.nome}')
        print(f'CPF: {self.paciente.cpf}')
        print(f'Idade: {self.paciente.idade}')
        print(f'Descrição: {self.descricao}')
        print(f'Resultado: {self.resultado}')


paciente = Paciente('Marcelo Silva', '033444555-22', 26)
medico = Medico('Ana Beatriz', 333431, 'Clínico Geral')
exame01 = Exame(medico, paciente, 'COVID-19', 'Negativo') 
exame01.imprimir_exame()
