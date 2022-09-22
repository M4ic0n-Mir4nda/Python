# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1:
# ALUNO 2:
# ALUNO 3:
# ALUNO 4:
# ALUNO 5:
# ALUNO 6: 


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
    
    def calcular_total(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        numero_letras = 0
        for indice in range(len(self.frase)):
            if self.frase[indice] == ' ':
                continue
            numero_letras += 1
        custo_desenho = numero_letras * self.__valor_fixo_letra
        valor_placa = custo_material + custo_desenho
        return valor_placa


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        total = 0
        for faturamento in self.__pedidos:
            total += faturamento
        return total
